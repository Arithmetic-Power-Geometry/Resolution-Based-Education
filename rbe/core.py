# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Hashable, Iterable, List, Mapping, Sequence, Tuple

World = Hashable
Decision = Hashable
Observation = Hashable


@dataclass(frozen=True)
class Intervention:
    name: str
    cost: float
    leakage: float
    observations: Mapping[World, Observation]

    def burden(self, leakage_weight: float = 1.0) -> float:
        return float(self.cost) + leakage_weight * float(self.leakage)


def observational_partition(
    worlds: Iterable[World],
    observations: Mapping[World, Observation],
) -> List[frozenset[World]]:
    buckets: Dict[Observation, set[World]] = {}
    for world in worlds:
        buckets.setdefault(observations[world], set()).add(world)
    return [frozenset(v) for v in buckets.values()]


def has_carg(
    worlds: Iterable[World],
    observations: Mapping[World, Observation],
    certification: Mapping[World, Decision],
) -> bool:
    """Return True when an observational equivalence class mixes decisions."""
    for cell in observational_partition(worlds, observations):
        if len({certification[w] for w in cell}) > 1:
            return True
    return False


def unresolved_pairs(
    worlds: Iterable[World],
    observations: Mapping[World, Observation],
    certification: Mapping[World, Decision],
) -> List[Tuple[World, World]]:
    """Certification-incompatible world pairs that the current protocol cannot distinguish."""
    result: List[Tuple[World, World]] = []
    for cell in observational_partition(worlds, observations):
        for i, wi in enumerate(sorted(cell, key=str)):
            for wj in sorted(cell, key=str)[i + 1 :]:
                if certification[wi] != certification[wj]:
                    result.append((wi, wj))
    return result


def intervention_separates(
    intervention: Intervention,
    pairs: Sequence[Tuple[World, World]],
) -> bool:
    return all(
        intervention.observations[wi] != intervention.observations[wj]
        for wi, wj in pairs
    )


def choose_mrrp(
    interventions: Iterable[Intervention],
    pairs: Sequence[Tuple[World, World]],
    leakage_weight: float = 1.0,
) -> Intervention:
    """Choose the least-burden intervention that separates every required pair.

    This is a deliberately minimal reference implementation for deterministic
    toy worlds. Real deployments should use probabilistic observations,
    uncertainty, fairness constraints, and validated psychometric models.
    """
    feasible = [i for i in interventions if intervention_separates(i, pairs)]
    if not feasible:
        raise ValueError("No supplied intervention restores the required resolution.")
    return min(feasible, key=lambda i: (i.burden(leakage_weight), i.name))
