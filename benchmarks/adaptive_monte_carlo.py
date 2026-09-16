# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under Apache-2.0.
"""Reproducible Monte Carlo comparison of adaptive RBE and fixed protocols.
Synthetic mechanism validation only; not human educational evidence.
"""
from __future__ import annotations
import csv, random
from pathlib import Path

WORLDS=("W1","W2","W3","W4")
CERT={"W1":1,"W2":1,"W3":0,"W4":0}
PROBES={
 "wrong-ai-check":({"W1":.90,"W2":.65,"W3":.55,"W4":.20},.55),
 "constraint-shift":({"W1":.94,"W2":.88,"W3":.20,"W4":.12},1.10),
 "transfer":({"W1":.90,"W2":.82,"W3":.30,"W4":.22},1.25),
 "generic-viva":({"W1":.95,"W2":.91,"W3":.16,"W4":.10},6.00),
}

def update(post, probe, positive):
    probs,_=PROBES[probe]; out={}
    for w,p in post.items():
        like=probs[w] if positive else 1-probs[w]
        out[w]=p*like
    z=sum(out.values())
    return {w:v/z for w,v in out.items()}

def p_cert(post): return sum(p for w,p in post.items() if CERT[w])

def decision(post, threshold=.90):
    p=p_cert(post)
    if p>=threshold:return 1
    if p<=1-threshold:return 0
    return None

def run_protocol(world, protocol, rng, threshold=.90):
    post={w:.25 for w in WORLDS}; burden=0.; used=0
    for probe in protocol:
        probs,cost=PROBES[probe]
        obs=rng.random()<probs[world]
        post=update(post,probe,obs); burden+=cost; used+=1
        if decision(post,threshold) is not None: break
    d=decision(post,threshold)
    return d, burden, used

def simulate(n=20000, seed=20260916, threshold=.90):
    rng=random.Random(seed)
    protocols={
      "adaptive_rbe":["constraint-shift","wrong-ai-check","transfer","generic-viva"],
      "fixed_targeted":["wrong-ai-check","constraint-shift","transfer"],
      "fixed_viva":["generic-viva"],
    }
    agg={k:{"errors":0,"resolved":0,"burden":0.,"probes":0} for k in protocols}
    for _ in range(n):
        world=rng.choice(WORLDS)
        for name,seq in protocols.items():
            d,b,u=run_protocol(world,seq,rng,threshold)
            a=agg[name]; a["burden"]+=b; a["probes"]+=u
            if d is not None:
                a["resolved"]+=1; a["errors"]+=int(d!=CERT[world])
    rows=[]
    for name,a in agg.items():
        rows.append({"protocol":name,"n":n,"threshold":threshold,
          "resolved_rate":a["resolved"]/n,
          "unresolved_rate":1-a["resolved"]/n,
          "decision_error_rate_all":a["errors"]/n,
          "decision_error_rate_resolved":a["errors"]/a["resolved"] if a["resolved"] else 0,
          "mean_burden":a["burden"]/n,"mean_probes":a["probes"]/n})
    return rows

def main():
    rows=simulate()
    out=Path("reports/adaptive_monte_carlo_results.csv")
    out.parent.mkdir(exist_ok=True)
    with out.open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    for r in rows: print(r)
if __name__=="__main__": main()
