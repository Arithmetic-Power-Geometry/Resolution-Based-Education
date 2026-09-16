# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from rbe.core import Intervention, choose_mrrp, has_carg, unresolved_pairs


def toy_worlds():
    worlds = ["W1", "W2", "W3", "W4"]
    certification = {"W1": 1, "W2": 1, "W3": 0, "W4": 0}
    artifact = {w: "excellent" for w in worlds}
    return worlds, certification, artifact


def test_artifact_only_protocol_has_carg():
    worlds, certification, artifact = toy_worlds()
    assert has_carg(worlds, artifact, certification)
    assert len(unresolved_pairs(worlds, artifact, certification)) == 4


def test_mrrp_selects_cheapest_full_separator():
    worlds, certification, artifact = toy_worlds()
    pairs = unresolved_pairs(worlds, artifact, certification)

    interventions = [
        Intervention(
            "generic-viva",
            cost=5.0,
            leakage=1.0,
            observations={"W1": "P", "W2": "P", "W3": "F", "W4": "F"},
        ),
        Intervention(
            "targeted-perturbation",
            cost=2.0,
            leakage=0.2,
            observations={"W1": "P", "W2": "P", "W3": "F", "W4": "F"},
        ),
    ]

    best = choose_mrrp(interventions, pairs, leakage_weight=1.0)
    assert best.name == "targeted-perturbation"


def test_no_carg_when_observation_resolves_certification():
    worlds, certification, _ = toy_worlds()
    resolved = {"W1": "pass-evidence", "W2": "pass-evidence", "W3": "fail-evidence", "W4": "fail-evidence"}
    assert not has_carg(worlds, resolved, certification)
