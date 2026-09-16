"""Final statistical stop gate for RBE real-data evidence efficiency.

Paired bootstrap over held-out OULAD students for the primary configuration
(cutoff=120, all outcomes, epsilon=.20). Tests the evidence-burden reduction
of adaptive acquisition relative to collecting all six evidence channels.
The result does NOT test predictive superiority and OULAD is observational.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from benchmarks.oulad_final_comparison import download, build_features, split, learn_order, adaptive_predictions, SEED

OUT = "reports/oulad_burden_bootstrap_results.csv"
N_BOOT = 5000


def paired_bootstrap_saving(used, fixed_burden, n_boot=N_BOOT, seed=SEED+991):
    used=np.asarray(used,float)
    saving=fixed_burden-used
    rng=np.random.default_rng(seed)
    means=np.empty(n_boot,float)
    n=len(saving)
    for b in range(n_boot):
        idx=rng.integers(0,n,n)
        means[b]=saving[idx].mean()
    lo,hi=np.quantile(means,[.025,.975])
    # One-sided empirical null probability that saving <= 0; report with +1 correction.
    p=(1+np.sum(means<=0))/(n_boot+1)
    return float(saving.mean()),float(lo),float(hi),float(p)


def main():
    z=download(); df=build_features(z,120,False)
    train,val,test=split(df); trainfull=pd.concat([train,val],ignore_index=True)
    order,_=learn_order(train,val)
    _,used,resolved=adaptive_predictions(trainfull,test,order,.20)
    fixed=float(len(order))
    mean,lo,hi,p=paired_bootstrap_saving(used,fixed)
    row=dict(cutoff=120,completers_only=False,epsilon=.20,n=len(test),n_boot=N_BOOT,
             fixed_all_burden=fixed,rbe_mean_burden=float(np.mean(used)),
             mean_burden_saving=mean,relative_saving=mean/fixed,
             ci95_low=lo,ci95_high=hi,bootstrap_p_saving_le_zero=p,
             rbe_resolved_coverage=float(np.mean(resolved)))
    out=pd.DataFrame([row]); out.to_csv(OUT,index=False)
    print(out.to_string(index=False)); print("Saved",OUT)

if __name__ == "__main__": main()
