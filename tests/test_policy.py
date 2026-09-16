# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from rbe.core import Intervention
from rbe.policy import minimum_resolution_policy


def test_policy_can_resolve_when_no_single_probe_fully_resolves():
    worlds = ["w1", "w2", "w3", "w4"]
    certification = {"w1": True, "w2": True, "w3": False, "w4": False}
    # p1 separates w1/w3 but leaves w2/w4 mixed; p2 resolves the remaining branch.
    p1 = Intervention("p1", 1.0, 0.0, {"w1": "a", "w2": "b", "w3": "c", "w4": "b"})
    p2 = Intervention("p2", 1.0, 0.0, {"w1": "x", "w2": "x", "w3": "x", "w4": "y"})
    result = minimum_resolution_policy(worlds, certification, [p1, p2])
    assert result.resolved
    assert result.first_probe == "p1"
    assert result.expected_burden == 1.5


def test_policy_reports_infeasible():
    worlds = ["w1", "w2"]
    certification = {"w1": True, "w2": False}
    useless = Intervention("u", 1.0, 0.0, {"w1": "same", "w2": "same"})
    result = minimum_resolution_policy(worlds, certification, [useless])
    assert not result.resolved
