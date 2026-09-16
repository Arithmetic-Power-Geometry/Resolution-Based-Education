# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from rbe.attainment import LearnerRCOResult, RBEState, course_metrics, weighted_programme_metric


def test_positive_resolution_is_required_for_rca():
    positive = LearnerRCOResult("A", "RCO1", 82, 60, 0.05, 0.10, True)
    negative = LearnerRCOResult("B", "RCO1", 82, 60, 0.05, 0.10, False)
    assert positive.rca == 1
    assert positive.state == RBEState.AR
    assert negative.rca == 0
    assert negative.state == RBEState.RN


def test_unresolved_and_not_attained_states():
    unresolved = LearnerRCOResult("A", "RCO1", 82, 60, 0.30, 0.10, None)
    not_attained = LearnerRCOResult("B", "RCO1", 52, 60, 0.05, 0.10, False)
    assert unresolved.state == RBEState.AU
    assert not_attained.state == RBEState.NA


def test_course_metrics_keep_states_distinct():
    rows = [
        LearnerRCOResult("A", "RCO1", 82, 60, 0.05, 0.10, True, burden=1.0),
        LearnerRCOResult("B", "RCO1", 82, 60, 0.20, 0.10, None, burden=2.0),
        LearnerRCOResult("C", "RCO1", 75, 60, 0.04, 0.10, False, burden=1.0),
        LearnerRCOResult("D", "RCO1", 52, 60, None, None, None, burden=0.0),
    ]
    m = course_metrics(rows)
    assert m["PAR"] == 0.75
    assert m["RR"] == 0.50
    assert m["RAR"] == 0.25
    assert m["UAR"] == 0.25
    assert m["RNR"] == 0.25
    assert m["MRB"] == 1.0


def test_weighted_programme_metric():
    value = weighted_programme_metric({"RCO1": 0.8, "RCO2": 0.6}, {"RCO1": 3, "RCO2": 1})
    assert abs(value - 0.75) < 1e-12
