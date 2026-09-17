# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import inf
from typing import Hashable, Mapping, Sequence

from .core import Intervention

World = Hashable
Decision = Hashable


@dataclass(frozen=True)
class PolicyResult:
    expected_burden: float
    first_probe: str | None
    resolved: bool


def optimal_resolution_policy(
    worlds: Sequence[World],
    certification: Mapping[World, Decision],
    interventions: Sequence[Intervention],
    leakage_weight: float = 1.0,
) -> PolicyResult:
    """Exact expected-burden policy search for small deterministic world sets.

    Worlds are assumed equally likely within the currently compatible set.
    Terminal nodes are certification-homogeneous. This implementation is for
    small auditable mechanism tests, not large-scale production deployment.
    """
    world_tuple = tuple(worlds)
    by_name = {i.name: i for i in interventions}

    def homogeneous(state: tuple[World, ...]) -> bool:
        return len({certification[w] for w in state}) <= 1

    @lru_cache(maxsize=None)
    def solve(state: tuple[World, ...], remaining: tuple[str, ...]) -> tuple[float, str | None, bool]:
        if homogeneous(state):
            return 0.0, None, True
        if not remaining:
            return inf, None, False

        best = (inf, None, False)
        for name in remaining:
            intervention = by_name[name]
            buckets: dict[object, list[World]] = {}
            for w in state:
                buckets.setdefault(intervention.observations[w], []).append(w)
            if len(buckets) <= 1:
                continue

            next_remaining = tuple(n for n in remaining if n != name)
            expected_future = 0.0
            feasible = True
            for bucket in buckets.values():
                substate = tuple(bucket)
                sub_cost, _, sub_resolved = solve(substate, next_remaining)
                if not sub_resolved:
                    feasible = False
                    break
                expected_future += (len(bucket) / len(state)) * sub_cost
            if not feasible:
                continue

            total = intervention.burden(leakage_weight) + expected_future
            candidate = (total, name, True)
            if candidate[0] < best[0] or (candidate[0] == best[0] and str(candidate[1]) < str(best[1])):
                best = candidate
        return best

    burden, first, resolved = solve(world_tuple, tuple(sorted(by_name)))
    return PolicyResult(expected_burden=burden, first_probe=first, resolved=resolved)
