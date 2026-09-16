# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
"""Probabilistic decision-resolution utilities for RBE.

This module extends deterministic MRRP to noisy learner responses. It does not
claim a new generic experiment-design algorithm; it operationalizes the RBE
question: which low-burden probe most reduces certification ambiguity?
"""
from __future__ import annotations

from dataclasses import dataclass
from math import log2
from typing import Hashable, Mapping, Sequence

World = Hashable
Decision = Hashable


@dataclass(frozen=True)
class ProbabilisticProbe:
    name: str
    cost: float
    leakage: float
    # Probability of a positive response for each learner world.
    p_positive: Mapping[World, float]

    def burden(self, leakage_weight: float = 1.0) -> float:
        return float(self.cost) + leakage_weight * float(self.leakage)


def _entropy_binary(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log2(p) - (1.0 - p) * log2(1.0 - p)


def decision_entropy(worlds: Sequence[World], prior: Mapping[World, float], certification: Mapping[World, Decision]) -> float:
    masses = {}
    total = sum(prior[w] for w in worlds)
    if total <= 0:
        raise ValueError("Prior mass must be positive.")
    for w in worlds:
        masses[certification[w]] = masses.get(certification[w], 0.0) + prior[w] / total
    return -sum(p * log2(p) for p in masses.values() if p > 0.0)


def expected_decision_entropy(worlds: Sequence[World], prior: Mapping[World, float], certification: Mapping[World, Decision], probe: ProbabilisticProbe) -> float:
    total = sum(prior[w] for w in worlds)
    norm = {w: prior[w] / total for w in worlds}
    p_pos = sum(norm[w] * probe.p_positive[w] for w in worlds)
    result = 0.0
    for positive, p_obs in ((True, p_pos), (False, 1.0 - p_pos)):
        if p_obs <= 0.0:
            continue
        posterior = {}
        for w in worlds:
            likelihood = probe.p_positive[w] if positive else 1.0 - probe.p_positive[w]
            posterior[w] = norm[w] * likelihood / p_obs
        result += p_obs * decision_entropy(worlds, posterior, certification)
    return result


def decision_information_gain(worlds: Sequence[World], prior: Mapping[World, float], certification: Mapping[World, Decision], probe: ProbabilisticProbe) -> float:
    return decision_entropy(worlds, prior, certification) - expected_decision_entropy(worlds, prior, certification, probe)


def choose_cheapest_informative_probe(worlds: Sequence[World], prior: Mapping[World, float], certification: Mapping[World, Decision], probes: Sequence[ProbabilisticProbe], leakage_weight: float = 1.0, min_information_gain: float = 0.05) -> ProbabilisticProbe:
    """Cheapest probe meeting a declared decision-information threshold."""
    feasible = [p for p in probes if decision_information_gain(worlds, prior, certification, p) >= min_information_gain]
    if not feasible:
        raise ValueError("No probe meets the required decision-information threshold.")
    return min(feasible, key=lambda p: (p.burden(leakage_weight), p.name))


def choose_best_efficiency_probe(worlds: Sequence[World], prior: Mapping[World, float], certification: Mapping[World, Decision], probes: Sequence[ProbabilisticProbe], leakage_weight: float = 1.0) -> ProbabilisticProbe:
    """Maximize expected certification-decision information per unit burden."""
    scored = []
    for p in probes:
        burden = max(p.burden(leakage_weight), 1e-12)
        scored.append((decision_information_gain(worlds, prior, certification, p) / burden, p.name, p))
    return max(scored, key=lambda x: (x[0], x[1]))[-1]
