"""Final real-data comparison for Resolution-Based Education (RBE).

Uses the public OULAD dataset (Kuzilek et al., 2017) downloaded from UCI.
This is an observational proxy benchmark, NOT a randomized OBE-vs-RBE trial.

Operational comparison:
  1. OBE-style fixed outcome-evidence baseline: early assessment score only.
  2. Enhanced fixed evidence: all pre-cutoff logged channels acquired for everyone.
  3. RBE adaptive resolution: begin with score evidence; acquire additional logged
     evidence in a validation-learned order and stop per student when posterior
     decision risk <= epsilon.
  4. Matched-budget fixed prefix: same approximate mean evidence-channel budget as RBE.

Primary scientific question:
Can adaptive resolution-seeking evidence acquisition attain comparable or lower
held-out certification decision risk with lower mean evidence burden than fixed
comprehensive acquisition?

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.
"""
from __future__ import annotations

import io
import math
import urllib.request
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, brier_score_loss, log_loss, roc_auc_score
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

URL = "https://archive.ics.uci.edu/static/public/349/open+university+learning+analytics+dataset.zip"
OUT = Path("reports/oulad_final_comparison_results.csv")
ORDER_OUT = Path("reports/oulad_rbe_acquisition_order.csv")
SEED = 20260916
BASE = ["score_mean"]
CANDIDATES = ["assessment_count", "vle_clicks", "active_days", "vle_records", "submission_lateness"]
ALL = BASE + CANDIDATES


def download():
    raw = urllib.request.urlopen(URL, timeout=120).read()
    return zipfile.ZipFile(io.BytesIO(raw))


def read(z, name):
    return pd.read_csv(z.open(name))


def build_features(z, cutoff=120, completers_only=False):
    info = read(z, "studentInfo.csv")
    assessments = read(z, "assessments.csv")[["code_module","code_presentation","id_assessment","date"]].copy()
    sa = read(z, "studentAssessment.csv")
    sv = read(z, "studentVle.csv")

    for c in ["date"]:
        assessments[c] = pd.to_numeric(assessments[c], errors="coerce")
    for c in ["date_submitted", "score"]:
        sa[c] = pd.to_numeric(sa[c], errors="coerce")
    for c in ["date", "sum_click"]:
        sv[c] = pd.to_numeric(sv[c], errors="coerce")

    keys = ["code_module","code_presentation","id_student"]
    a = sa.merge(assessments, on=["code_module","code_presentation","id_assessment"], how="left")
    # Evidence available by cutoff; scheduled assessment date prevents using future assessments.
    a = a[(a["date"].fillna(99999) <= cutoff) & (a["date_submitted"].fillna(99999) <= cutoff)].copy()
    a["lateness"] = a["date_submitted"] - a["date"]
    ag = a.groupby(keys, observed=True).agg(
        score_mean=("score","mean"),
        assessment_count=("id_assessment","nunique"),
        submission_lateness=("lateness","mean"),
    ).reset_index()

    v = sv[sv["date"].fillna(99999) <= cutoff].copy()
    vg = v.groupby(keys, observed=True).agg(
        vle_clicks=("sum_click","sum"),
        active_days=("date","nunique"),
        vle_records=("id_site","size"),
    ).reset_index()

    df = info.merge(ag, on=keys, how="left").merge(vg, on=keys, how="left")
    if completers_only:
        df = df[df["final_result"].isin(["Pass","Distinction","Fail"])].copy()
    df["certify"] = df["final_result"].isin(["Pass","Distinction"]).astype(int)
    # Counts are true zeros when no logged evidence occurred before cutoff.
    for c in ["assessment_count","vle_clicks","active_days","vle_records"]:
        df[c] = df[c].fillna(0)
    return df


def split(df):
    g1 = GroupShuffleSplit(n_splits=1, test_size=.20, random_state=SEED)
    trainval_idx, test_idx = next(g1.split(df, groups=df.id_student))
    trainval, test = df.iloc[trainval_idx].copy(), df.iloc[test_idx].copy()
    g2 = GroupShuffleSplit(n_splits=1, test_size=.25, random_state=SEED+1)
    tr_idx, va_idx = next(g2.split(trainval, groups=trainval.id_student))
    return trainval.iloc[tr_idx].copy(), trainval.iloc[va_idx].copy(), test


def model(features):
    prep = ColumnTransformer([("num", Pipeline([
        ("imp", SimpleImputer(strategy="median", add_indicator=True)),
        ("scale", StandardScaler()),
    ]), features)])
    return Pipeline([("prep", prep), ("clf", LogisticRegression(max_iter=1000, C=1.0, random_state=SEED))])


def fit_predict(train, eval_df, features):
    m = model(features)
    m.fit(train[features], train.certify)
    return m, m.predict_proba(eval_df[features])[:,1]


def metrics(y, p, mask=None):
    y = np.asarray(y); p = np.asarray(p)
    if mask is None: mask = np.ones(len(y), dtype=bool)
    yy, pp = y[mask], p[mask]
    if len(yy) == 0:
        return dict(coverage=0., risk=np.nan, accuracy=np.nan, brier=np.nan, logloss=np.nan, auc=np.nan)
    pred = (pp >= .5).astype(int)
    return dict(
        coverage=float(mask.mean()),
        risk=float(np.mean(pred != yy)),
        accuracy=float(accuracy_score(yy,pred)),
        brier=float(brier_score_loss(yy,pp)),
        logloss=float(log_loss(yy,pp,labels=[0,1])),
        auc=float(roc_auc_score(yy,pp)) if len(np.unique(yy)) > 1 else np.nan,
    )


def learn_order(train, val):
    chosen = BASE.copy(); remaining = CANDIDATES.copy(); rows=[]
    while remaining:
        scored=[]
        for f in remaining:
            _, p = fit_predict(train, val, chosen+[f])
            scored.append((brier_score_loss(val.certify,p), f))
        score, best = min(scored)
        chosen.append(best); remaining.remove(best)
        rows.append({"step":len(chosen)-1,"acquired":best,"validation_brier":score})
    return chosen, pd.DataFrame(rows)


def adaptive_predictions(train, test, order, epsilon):
    # Models are trained for every prefix. Each held-out student starts at the
    # baseline and stops as soon as posterior plug-in decision risk min(p,1-p)
    # is <= epsilon. If unresolved, the next evidence channel is acquired.
    probs=[]
    for k in range(1,len(order)+1):
        _, p=fit_predict(train,test,order[:k]); probs.append(p)
    P=np.vstack(probs)
    n=len(test); final=np.empty(n); used=np.empty(n,dtype=int); resolved=np.zeros(n,dtype=bool)
    for i in range(n):
        kstop=len(order)
        for k in range(len(order)):
            if min(P[k,i],1-P[k,i]) <= epsilon:
                kstop=k+1; resolved[i]=True; break
        final[i]=P[kstop-1,i]; used[i]=kstop
    return final, used, resolved


def run_one(z, cutoff, completers_only, epsilon):
    df=build_features(z,cutoff,completers_only)
    train,val,test=split(df)
    # Learn acquisition order without test labels, then refit on train+validation.
    order, order_df=learn_order(train,val)
    trainfull=pd.concat([train,val],ignore_index=True)
    y=test.certify.to_numpy()
    rows=[]

    def add(protocol,p,burden,resolved=None):
        mask=np.ones(len(y),dtype=bool) if resolved is None else resolved
        m=metrics(y,p,mask)
        rows.append(dict(cutoff=cutoff,completers_only=completers_only,epsilon=epsilon,
                         n=len(test),protocol=protocol,mean_evidence_burden=float(np.mean(burden)),**m))

    _, pbase=fit_predict(trainfull,test,BASE)
    add("OBE_style_score_baseline",pbase,np.ones(len(test)))
    _, pall=fit_predict(trainfull,test,order)
    add("enhanced_fixed_all_evidence",pall,np.full(len(test),len(order)))

    prbe, used, resolved=adaptive_predictions(trainfull,test,order,epsilon)
    # Report both selective resolved-only risk and forced final decision risk.
    add("RBE_adaptive_resolved",prbe,used,resolved)
    add("RBE_adaptive_forced",prbe,used)

    # Matched-budget fixed prefix: closest integer prefix to RBE mean channel count.
    k=max(1,min(len(order),int(round(float(np.mean(used))))))
    _, pmatch=fit_predict(trainfull,test,order[:k])
    add("fixed_matched_budget_prefix",pmatch,np.full(len(test),k))

    od=order_df.copy(); od["cutoff"]=cutoff; od["completers_only"]=completers_only; od["epsilon"]=epsilon
    return rows,od


def main():
    z=download(); all_rows=[]; orders=[]
    for cutoff in [60,90,120]:
        for completers in [False,True]:
            for eps in [.05,.10,.20]:
                rows,od=run_one(z,cutoff,completers,eps); all_rows.extend(rows); orders.append(od)
    out=pd.DataFrame(all_rows)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    out.to_csv(OUT,index=False)
    pd.concat(orders,ignore_index=True).to_csv(ORDER_OUT,index=False)
    print(out.to_string(index=False))
    print("\nSaved",OUT,"and",ORDER_OUT)

if __name__ == "__main__":
    main()
