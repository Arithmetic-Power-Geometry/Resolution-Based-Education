# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class RBEState(str, Enum):
    AR = "AR"          # attained, resolved-positive
    AU = "AU"          # attained, unresolved
    RN = "RN"          # attained, resolved-negative
    NA = "NA"          # not attained
    DEFERRED = "Deferred"


@dataclass(frozen=True)
class LearnerRCOResult:
    score: float
    threshold: float
    decision_risk: float | None = None
    epsilon: float | None = None
    resolved_decision_positive: bool | None = None
    burden: float = 0.0
    deferred: bool = False

    @property
    def performance_attained(self) -> bool:
        return self.score >= self.threshold

    @property
    def resolved(self) -> bool:
        return (
            self.decision_risk is not None
            and self.epsilon is not None
            and self.decision_risk <= self.epsilon
            and self.resolved_decision_positive is not None
        )

    @property
    def resolved_positive(self) -> bool:
        return self.resolved and self.resolved_decision_positive is True

    @property
    def rca(self) -> int:
        return int(self.performance_attained and self.resolved_positive)

    @property
    def state(self) -> RBEState:
        if self.deferred:
            return RBEState.DEFERRED
        if not self.performance_attained:
            return RBEState.NA
        if not self.resolved:
            return RBEState.AU
        return RBEState.AR if self.resolved_decision_positive else RBEState.RN


def course_metrics(results: Iterable[LearnerRCOResult]) -> dict[str, float]:
    records = list(results)
    if not records:
        raise ValueError("At least one learner record is required.")
    n = len(records)
    attained = [r for r in records if r.performance_attained]
    return {
        "PAR": sum(r.performance_attained for r in records) / n,
        "RR": sum(r.resolved for r in records) / n,
        "RAR": sum(r.rca for r in records) / n,
        "UAR": sum(r.state == RBEState.AU for r in records) / n,
        "RNR": sum(r.state == RBEState.RN for r in records) / n,
        "DR": sum(r.state == RBEState.DEFERRED for r in records) / n,
        "MRB": sum(r.burden for r in records) / n,
        "attained_count": float(len(attained)),
    }


def weighted_programme_metric(values: Iterable[float], weights: Iterable[float]) -> float:
    vals = list(values)
    wts = list(weights)
    if len(vals) != len(wts) or not vals:
        raise ValueError("Values and weights must be non-empty and have equal length.")
    total = sum(wts)
    if total <= 0:
        raise ValueError("Sum of weights must be positive.")
    return sum(v * w for v, w in zip(vals, wts)) / total
