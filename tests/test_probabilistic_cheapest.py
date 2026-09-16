# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from rbe.probabilistic import (
    ProbabilisticProbe,
    choose_best_efficiency_probe,
    choose_cheapest_informative_probe,
    decision_entropy,
    decision_information_gain,
)

WORLDS = ["W1", "W2", "W3", "W4"]
CERT = {"W1": 1, "W2": 1, "W3": 0, "W4": 0}
PRIOR = {w: 0.25 for w in WORLDS}


def probes():
    return [
        ProbabilisticProbe("wrong-ai-check", 0.50, 0.05, {"W1": .90, "W2": .65, "W3": .55, "W4": .20}),
        ProbabilisticProbe("constraint-shift", 1.00, 0.10, {"W1": .94, "W2": .88, "W3": .20, "W4": .12}),
        ProbabilisticProbe("transfer", 1.15, 0.10, {"W1": .90, "W2": .82, "W3": .30, "W4": .22}),
        ProbabilisticProbe("generic-viva", 5.00, 1.00, {"W1": .95, "W2": .91, "W3": .16, "W4": .10}),
    ]


def test_initial_certification_uncertainty_is_one_bit():
    assert abs(decision_entropy(WORLDS, PRIOR, CERT) - 1.0) < 1e-12


def test_all_declared_probes_reduce_decision_uncertainty():
    for p in probes():
        assert decision_information_gain(WORLDS, PRIOR, CERT, p) > 0.0


def test_cheapest_probe_depends_on_required_resolution():
    # At a modest evidence requirement the cheap wrong-AI probe is sufficient.
    low = choose_cheapest_informative_probe(WORLDS, PRIOR, CERT, probes(), min_information_gain=0.10)
    assert low.name == "wrong-ai-check"
    # At a stronger evidence requirement it is no longer sufficient; the
    # constraint-shift becomes the cheapest qualifying probe.
    high = choose_cheapest_informative_probe(WORLDS, PRIOR, CERT, probes(), min_information_gain=0.30)
    assert high.name == "constraint-shift"


def test_resolution_efficiency_beats_generic_viva_on_declared_model():
    best = choose_best_efficiency_probe(WORLDS, PRIOR, CERT, probes())
    assert best.name in {"wrong-ai-check", "constraint-shift"}
    viva = next(p for p in probes() if p.name == "generic-viva")
    assert decision_information_gain(WORLDS, PRIOR, CERT, best) / best.burden() > decision_information_gain(WORLDS, PRIOR, CERT, viva) / viva.burden()


def test_artifact_only_has_zero_decision_information():
    artifact = ProbabilisticProbe("artifact-only", 0.0, 0.0, {w: .92 for w in WORLDS})
    assert abs(decision_information_gain(WORLDS, PRIOR, CERT, artifact)) < 1e-12
