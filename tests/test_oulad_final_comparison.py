"""Offline tests for the final OULAD comparison logic.
Copyright (C) 2026 Mohammad Amir Khusru Akhtar. Apache-2.0.
"""
import numpy as np
import pandas as pd
from benchmarks.oulad_final_comparison import metrics


def test_selective_risk_uses_only_resolved_cases():
    y=np.array([1,0,1,0]); p=np.array([.99,.01,.51,.49]); mask=np.array([1,1,0,0],dtype=bool)
    m=metrics(y,p,mask)
    assert m["coverage"] == .5
    assert m["risk"] == 0.0


def test_forced_metric_covers_every_case():
    y=np.array([1,0,1,0]); p=np.array([.9,.1,.6,.4])
    assert metrics(y,p)["coverage"] == 1.0


def test_error_is_not_hidden_by_accuracy():
    y=np.array([1,1,0,0]); p=np.array([.9,.4,.2,.8])
    m=metrics(y,p)
    assert np.isclose(m["risk"],1-m["accuracy"])


def test_brier_is_properly_bounded():
    y=np.array([1,0]); p=np.array([.8,.2])
    assert 0 <= metrics(y,p)["brier"] <= 1
