# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under Apache-2.0.
"""Real-data RBE resolution benchmark for OULAD.

Downloads the public OULAD CSV archive at runtime (data are not redistributed).
Uses only pre-outcome behavioural/assessment evidence to construct an auditable
proxy experiment-selection benchmark. This is observational validation of the
resolution machinery, NOT a causal trial of RBE and NOT an AI-use dataset.

Official dataset: https://analyse.kmi.open.ac.uk/open-dataset
Citation: Kuzilek, Hlosta & Zdrahal (2017), Scientific Data 4, 170171.
"""
from __future__ import annotations
import io, urllib.request, zipfile
import pandas as pd
import numpy as np

URL="https://analyse.kmi.open.ac.uk/open_dataset/download"

def load():
    raw=urllib.request.urlopen(URL,timeout=90).read()
    z=zipfile.ZipFile(io.BytesIO(raw))
    info=pd.read_csv(z.open("studentInfo.csv"))
    sa=pd.read_csv(z.open("studentAssessment.csv"))
    ass=pd.read_csv(z.open("assessments.csv"))
    sv=pd.read_csv(z.open("studentVle.csv"))
    return info,sa,ass,sv

def build_table(info,sa,ass,sv):
    a=sa.merge(ass,on="id_assessment",how="left")
    # Early/mid-course assessment evidence; avoid final exam/CMA leakage where possible.
    a=a[(a["date"].fillna(9999)<=120)&a["score"].notna()]
    ag=a.groupby(["code_module","code_presentation","id_student"]).agg(
        assess_mean=("score","mean"), assess_n=("score","size"),
        late_mean=("date_submitted",lambda x: float(np.mean(x)))
    ).reset_index()
    v=sv[sv["date"]<=120].groupby(["code_module","code_presentation","id_student"]).agg(
        vle_clicks=("sum_click","sum"), active_days=("date","nunique")
    ).reset_index()
    d=info.merge(ag,on=["code_module","code_presentation","id_student"],how="left").merge(v,on=["code_module","code_presentation","id_student"],how="left")
    d["certify"] = d["final_result"].isin(["Pass","Distinction"]).astype(int)
    for c in ["assess_mean","assess_n","late_mean","vle_clicks","active_days"]: d[c]=d[c].fillna(0)
    return d

def qbin(s,q=5):
    return pd.qcut(s.rank(method="first"),q,labels=False,duplicates="drop").astype(int)

def unresolved_rate(d, cols):
    x=d.copy()
    for c in cols: x[c+"_bin"]=qbin(x[c])
    keys=[c+"_bin" for c in cols]
    g=x.groupby(keys)["certify"].agg(["min","max","size"]).reset_index()
    bad=g[g["min"]!=g["max"]]
    unresolved=int(bad["size"].sum())
    return unresolved/len(x), unresolved, len(bad)

def evaluate():
    d=build_table(*load())
    base=["assess_mean"]
    candidates={
      "assessment_count":["assess_n"],
      "vle_engagement":["vle_clicks"],
      "active_days":["active_days"],
      "submission_timing":["late_mean"],
    }
    r0,n0,c0=unresolved_rate(d,base)
    rows=[]
    # Cost is declared evidence-acquisition burden proxy; existing logged evidence=1.
    for name,extra in candidates.items():
        r,n,c=unresolved_rate(d,base+extra)
        rows.append({"experiment":name,"n_students":len(d),"base_unresolved_rate":r0,
                     "post_unresolved_rate":r,"absolute_resolution_gain":r0-r,
                     "remaining_unresolved_students":n,"mixed_cells":c,"declared_cost":1.0,
                     "gain_per_cost":r0-r})
    return pd.DataFrame(rows).sort_values(["gain_per_cost","experiment"],ascending=[False,True])

if __name__=="__main__":
    out=evaluate(); print(out.to_string(index=False)); out.to_csv("reports/oulad_resolution_results.csv",index=False)
