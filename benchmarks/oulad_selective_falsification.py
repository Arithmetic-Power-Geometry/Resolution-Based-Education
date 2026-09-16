"""Final falsification gate for the OULAD RBE benchmark.

Tests whether the apparent low-risk RBE resolved subset adds value beyond:
(1) ordinary confidence-based selective prediction using fixed all evidence, and
(2) random evidence-acquisition orders at matched coverage/burden.

This is retrospective observational evidence, not a randomized educational trial.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from benchmarks.oulad_final_comparison import (
    download, build_features, split, learn_order, fit_predict,
    adaptive_predictions, metrics, BASE, CANDIDATES, SEED,
)

OUT = "reports/oulad_selective_falsification_results.csv"


def top_confidence_mask(p, coverage):
    n = len(p); k = max(1, int(round(coverage*n)))
    conf = np.abs(np.asarray(p)-0.5)
    idx = np.argsort(-conf)[:k]
    mask = np.zeros(n, dtype=bool); mask[idx] = True
    return mask


def run(cutoff=120, completers=False, epsilon=.20, n_random=100):
    z=download(); df=build_features(z,cutoff,completers)
    train,val,test=split(df); trainfull=pd.concat([train,val],ignore_index=True)
    order,_=learn_order(train,val); y=test.certify.to_numpy()
    prbe,used,resolved=adaptive_predictions(trainfull,test,order,epsilon)
    rbe=metrics(y,prbe,resolved); burden=float(np.mean(used)); coverage=rbe["coverage"]

    # Fair ordinary selective baseline: all evidence, then select exactly the same
    # fraction of most confident held-out cases. This isolates selection/abstention.
    _,pall=fit_predict(trainfull,test,order)
    fixed_mask=top_confidence_mask(pall,coverage)
    fixed=metrics(y,pall,fixed_mask)

    # Random acquisition-order null. BASE is always first; remaining channels shuffled.
    rng=np.random.default_rng(SEED+77); random_rows=[]
    for r in range(n_random):
        cand=CANDIDATES.copy(); rng.shuffle(cand); ro=BASE+cand
        p,u,res=adaptive_predictions(trainfull,test,ro,epsilon)
        m=metrics(y,p,res)
        random_rows.append((m["risk"],m["coverage"],float(np.mean(u))))
    rr=np.asarray(random_rows,float)

    rows=[
      dict(test="RBE_adaptive",cutoff=cutoff,completers_only=completers,epsilon=epsilon,n=len(test),risk=rbe["risk"],coverage=coverage,mean_burden=burden),
      dict(test="fixed_all_confidence_matched_coverage",cutoff=cutoff,completers_only=completers,epsilon=epsilon,n=len(test),risk=fixed["risk"],coverage=fixed["coverage"],mean_burden=float(len(order))),
      dict(test="random_order_mean",cutoff=cutoff,completers_only=completers,epsilon=epsilon,n=len(test),risk=float(np.nanmean(rr[:,0])),coverage=float(np.nanmean(rr[:,1])),mean_burden=float(np.mean(rr[:,2]))),
      dict(test="random_order_best_risk",cutoff=cutoff,completers_only=completers,epsilon=epsilon,n=len(test),risk=float(np.nanmin(rr[:,0])),coverage=float(rr[np.nanargmin(rr[:,0]),1]),mean_burden=float(rr[np.nanargmin(rr[:,0]),2])),
    ]
    return pd.DataFrame(rows)


def main():
    frames=[]
    for cutoff in [60,90,120]:
      for comp in [False,True]:
        for eps in [.10,.20]: frames.append(run(cutoff,comp,eps))
    out=pd.concat(frames,ignore_index=True); out.to_csv(OUT,index=False)
    print(out.to_string(index=False)); print("Saved",OUT)

if __name__ == "__main__": main()
