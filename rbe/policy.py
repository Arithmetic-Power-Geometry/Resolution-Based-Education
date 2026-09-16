# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
"""Adaptive resolution-policy utilities for RBE.

The framework distinguishes a one-step discriminating probe from a true
resolution-restoring policy. A one-step probe may be informative yet still fail
to reach the declared stopping criterion. This module provides a small exact
search over deterministic toy worlds so that the distinction is executable and
testable.
"""
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


def _homogeneous(worlds: Sequence[World], certification: Mapping[World, Decision]) -> bool:
    return bool(worlds) and len({certification[w] for w in worlds}) == 1


def minimum_resolution_policy(
    worlds: Sequence[World],
    certification: Mapping[World, Decision],
    interventions: Sequence[Intervention],
    leakage_weight: float = 1.0,
) -> PolicyResult:
    """Exact minimum expected-burden adaptive policy for deterministic toy worlds.

    Worlds are given equal prior mass. Each probe branches on its deterministic
    observation. A feasible policy must end only in certification-homogeneous
    leaves. The returned first_probe is the root action of the optimal policy.
    """
    world_tuple = tuple(worlds)
    by_name = {p.name: p for p in interventions}
    probe_names = tuple(sorted(by_name))

    @lru_cache(maxsize=None)
    def solve(state: tuple[World, ...], remaining: tuple[str, ...]) -> tuple[float, str | None, bool]:
        if _homogeneous(state, certification):
            return 0.0, None, True
        if not remaining:
            return inf, None, False

        best = (inf, None, False)
        for name in remaining:
            probe = by_name[name]
            buckets: dict[object, list[World]] = {}
            for w in state:
                buckets.setdefault(probe.observations[w], []).append(w)
            if len(buckets) <= 1:
                continue

            next_remaining = tuple(x for x in remaining if x != name)
            expected_future = 0.0
            feasible = True
            for bucket in buckets.values():
                cost, _, ok = solve(tuple(bucket), next_remaining)
                if not ok:
                    feasible = False
                    break
                expected_future += (len(bucket) / len(state)) * cost
            if not feasible:
                continue
            total = probe.burden(leakage_weight) + expected_future
            candidate = (total, name, True)
            if total < best[0] or (total == best[0] and name < (best[1] or name)):
                best = candidate
        return best

    burden, root, ok = solve(world_tuple, probe_names)
    return PolicyResult(burden, root, ok)
