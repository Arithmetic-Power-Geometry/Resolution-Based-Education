# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under Apache-2.0.
"""Offline structural tests for the OULAD benchmark logic.
The full real-data benchmark is network-dependent and is run separately.
"""
import pandas as pd
from benchmarks.oulad_resolution_benchmark import unresolved_rate

def fixture():
    return pd.DataFrame({
      "assess_mean":[80,80,40,40,80,40],
      "vle_clicks":[100,10,100,10,90,20],
      "active_days":[20,2,20,2,18,3],
      "certify":[1,0,1,0,1,0],
    })

def test_added_evidence_can_reduce_decision_incompatibility():
    d=fixture(); base=unresolved_rate(d,["assess_mean"])[0]
    refined=unresolved_rate(d,["assess_mean","vle_clicks"])[0]
    assert refined <= base

def test_resolution_metric_is_bounded():
    r, n, cells=unresolved_rate(fixture(),["assess_mean"])
    assert 0 <= r <= 1 and n >= 0 and cells >= 0
