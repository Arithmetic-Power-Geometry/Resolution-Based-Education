# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under Apache-2.0.
"""Real-data RBE resolution benchmark for OULAD.
Observational proxy validation, not a causal RBE or AI-use trial.
Full-data workflow uses the UCI-hosted CC BY 4.0 OULAD archive.
"""
from __future__ import annotations
import io, urllib.request, zipfile
import pandas as pd

URL="https://archive.ics.uci.edu/static/public/349/open+university+learning+analytics+dataset.zip"

def load():
    req=urllib.request.Request(URL,headers={"User-Agent":"RBE-research/1.0"})
    raw=urllib.request.urlopen(req,timeout=180).read()
    z=zipfile.ZipFile(io.BytesIO(raw))
    names={n.split('/')[-1]:n for n in z.namelist()}
    info=pd.read_csv(z.open(names["studentInfo.csv"]))
    sa=pd.read_csv(z.open(names["studentAssessment.csv"]))
    ass=pd.read_csv(z.open(names["assessments.csv"]))
    sv=pd.read_csv(z.open(names["studentVle.csv"]))
    return info,sa,ass,sv

def build_table(info,sa,ass,sv,cutoff=120):
    # studentAssessment has date_submitted; assessments has the scheduled assessment date.
    # Merge with explicit suffixes so the scheduled date cannot silently become a string/object
    # or be confused with another date-like field after schema/library changes.
    a=sa.merge(
        ass[["id_assessment","code_module","code_presentation","assessment_type","date","weight"]],
        on="id_assessment",how="left",suffixes=("_student","_assessment")
    )
    scheduled_date="date"
    a[scheduled_date]=pd.to_numeric(a[scheduled_date],errors="coerce")
    a["score"]=pd.to_numeric(a["score"],errors="coerce")
    a["date_submitted"]=pd.to_numeric(a["date_submitted"],errors="coerce")
    a=a[(a[scheduled_date].fillna(9999)<=cutoff)&a["score"].notna()]
    ag=a.groupby(["code_module","code_presentation","id_student"]).agg(
        assess_mean=("score","mean"), assess_n=("score","size"), submission_mean=("date_submitted","mean")
    ).reset_index()
    sv=sv.copy()
    sv["date"]=pd.to_numeric(sv["date"],errors="coerce")
    sv["sum_click"]=pd.to_numeric(sv["sum_click"],errors="coerce").fillna(0)
    v=sv[sv["date"]<=cutoff].groupby(["code_module","code_presentation","id_student"]).agg(
        vle_clicks=("sum_click","sum"), active_days=("date","nunique"), vle_records=("date","size")
    ).reset_index()
    keys=["code_module","code_presentation","id_student"]
    d=info.merge(ag,on=keys,how="left").merge(v,on=keys,how="left")
    d["certify"]=d["final_result"].isin(["Pass","Distinction"]).astype(int)
    for c in ["assess_mean","assess_n","submission_mean","vle_clicks","active_days","vle_records"]:
        d[c]=pd.to_numeric(d[c],errors="coerce").fillna(0)
    return d

def qbin(s,q=5):
    return pd.qcut(s.rank(method="first"),q,labels=False,duplicates="drop").astype(int)

def unresolved_rate(d,cols,q=5):
    x=d.copy(); keys=[]
    for c in cols:
        k=c+"_bin"; x[k]=qbin(x[c],q); keys.append(k)
    g=x.groupby(keys)["certify"].agg(["min","max","size"]).reset_index()
    bad=g[g["min"]!=g["max"]]
    n=int(bad["size"].sum())
    return n/len(x),n,len(bad)

def evaluate(cutoff=120,q=5):
    d=build_table(*load(),cutoff=cutoff); base=["assess_mean"]
    candidates={
        "assessment_count":["assess_n"],
        "vle_engagement":["vle_clicks"],
        "active_days":["active_days"],
        "submission_timing":["submission_mean"],
        "vle_records":["vle_records"],
    }
    r0,_,_=unresolved_rate(d,base,q); rows=[]
    for name,extra in candidates.items():
        r,n,c=unresolved_rate(d,base+extra,q)
        rows.append({
            "experiment":name,"n_student_modules":len(d),"cutoff":cutoff,"q":q,
            "base_unresolved_rate":r0,"post_unresolved_rate":r,
            "absolute_resolution_gain":r0-r,"remaining_unresolved_students":n,
            "mixed_cells":c,"declared_cost":1.0,"gain_per_cost":r0-r,
        })
    return pd.DataFrame(rows).sort_values(["gain_per_cost","experiment"],ascending=[False,True])

if __name__=="__main__":
    out=evaluate()
    print(out.to_string(index=False))
    out.to_csv("reports/oulad_resolution_results.csv",index=False)
