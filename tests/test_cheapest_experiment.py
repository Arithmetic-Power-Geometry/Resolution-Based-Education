# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
"""Tests the RBE question: find the cheapest experiment under which
currently compatible certification-incompatible worlds disagree.

This is a constructed mechanism test, not human educational evidence.
"""
from rbe.core import Intervention, choose_mrrp, has_carg, unresolved_pairs


def setup_worlds():
    worlds = ["W1", "W2", "W3", "W4"]
    certification = {"W1": 1, "W2": 1, "W3": 0, "W4": 0}
    artifact = {w: "excellent" for w in worlds}
    return worlds, certification, artifact


def candidate_experiments():
    return [
        Intervention("generic-viva", 5.0, 1.0,
                     {"W1":"P","W2":"P","W3":"F","W4":"F"}),
        Intervention("constraint-shift", 1.0, 0.10,
                     {"W1":"P","W2":"P","W3":"F","W4":"F"}),
        # Cheaper, but insufficient: it distinguishes blind reliance only.
        Intervention("wrong-ai-check", 0.50, 0.05,
                     {"W1":"P","W2":"P","W3":"P","W4":"F"}),
        Intervention("transfer", 1.20, 0.05,
                     {"W1":"P","W2":"P","W3":"F","W4":"F"}),
    ]


def test_above_knowledge_leaves_mutually_incompatible_worlds():
    worlds, certification, artifact = setup_worlds()
    assert has_carg(worlds, artifact, certification)
    assert len(unresolved_pairs(worlds, artifact, certification)) == 4


def test_cheapest_experiment_is_not_merely_cheapest_probe():
    worlds, certification, artifact = setup_worlds()
    pairs = unresolved_pairs(worlds, artifact, certification)
    best = choose_mrrp(candidate_experiments(), pairs, leakage_weight=1.0)
    # wrong-ai-check has lower raw burden (0.55) but does not separate all
    # certification-incompatible worlds. constraint-shift is the cheapest
    # feasible full separator (1.10).
    assert best.name == "constraint-shift"
    assert abs(best.burden(1.0) - 1.10) < 1e-12


def test_selected_experiment_removes_carg_in_constructed_worlds():
    worlds, certification, artifact = setup_worlds()
    pairs = unresolved_pairs(worlds, artifact, certification)
    best = choose_mrrp(candidate_experiments(), pairs)
    assert not has_carg(worlds, best.observations, certification)


def test_leakage_weight_can_change_optimal_experiment():
    worlds, certification, artifact = setup_worlds()
    pairs = unresolved_pairs(worlds, artifact, certification)
    candidates = [
        Intervention("low-cost-high-leak", 0.50, 1.00,
                     {"W1":"P","W2":"P","W3":"F","W4":"F"}),
        Intervention("higher-cost-low-leak", 1.00, 0.05,
                     {"W1":"P","W2":"P","W3":"F","W4":"F"}),
    ]
    assert choose_mrrp(candidates, pairs, leakage_weight=0.1).name == "low-cost-high-leak"
    assert choose_mrrp(candidates, pairs, leakage_weight=1.0).name == "higher-cost-low-leak"
