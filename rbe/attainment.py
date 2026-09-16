# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
"""Attainment and certification-state utilities for Resolution-Based Education.

This module keeps performance attainment separate from certification resolution.
It implements the framework correction that a low decision-risk value alone does
not imply positive capability attainment: the resolved decision must support the
positive certification decision.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Mapping, Sequence


class RBEState(str, Enum):
    AR = "attained-resolved-positive"
    AU = "attained-unresolved"
    RN = "attained-resolved-negative"
    NA = "not-attained"
    DEFERRED = "deferred"


@dataclass(frozen=True)
class LearnerRCOResult:
    learner_id: str
    rco_id: str
    score: float
    performance_threshold: float
    decision_risk: float | None
    risk_threshold: float | None
    resolved_decision: bool | None
    burden: float = 0.0
    deferred: bool = False

    @property
    def performance_attained(self) -> bool:
        return self.score >= self.performance_threshold

    @property
    def resolved(self) -> bool:
        return (
            self.decision_risk is not None
            and self.risk_threshold is not None
            and self.decision_risk <= self.risk_threshold
            and self.resolved_decision is not None
        )

    @property
    def resolved_positive(self) -> bool:
        return self.resolved and bool(self.resolved_decision)

    @property
    def rca(self) -> int:
        """Resolved Capability Attainment indicator."""
        return int(self.performance_attained and self.resolved_positive)

    @property
    def state(self) -> RBEState:
        if self.deferred:
            return RBEState.DEFERRED
        if not self.performance_attained:
            return RBEState.NA
        if not self.resolved:
            return RBEState.AU
        return RBEState.AR if self.resolved_positive else RBEState.RN


def course_metrics(results: Sequence[LearnerRCOResult]) -> Mapping[str, float]:
    """Return PAR, RR, RAR, UAR, RNR, DR and mean resolution burden.

    Denominator is the number of learner-RCO records supplied. RNR is the
    performance-attained/resolved-negative rate. DR is deferred rate.
    """
    if not results:
        raise ValueError("At least one learner-RCO result is required.")
    n = len(results)
    par = sum(r.performance_attained for r in results) / n
    rr = sum(r.resolved for r in results) / n
    rar = sum(r.rca for r in results) / n
    uar = sum(r.state == RBEState.AU for r in results) / n
    rnr = sum(r.state == RBEState.RN for r in results) / n
    dr = sum(r.state == RBEState.DEFERRED for r in results) / n
    mrb = sum(r.burden for r in results) / n
    return {
        "PAR": par,
        "RR": rr,
        "RAR": rar,
        "UAR": uar,
        "RNR": rnr,
        "DR": dr,
        "MRB": mrb,
    }


def weighted_programme_metric(
    course_values: Mapping[str, float],
    mapping_weights: Mapping[str, float],
) -> float:
    """Weighted programme aggregation with explicit denominator semantics."""
    keys = [k for k in course_values if mapping_weights.get(k, 0.0) > 0.0]
    denom = sum(mapping_weights[k] for k in keys)
    if denom <= 0.0:
        raise ValueError("Positive mapping weight is required.")
    return sum(course_values[k] * mapping_weights[k] for k in keys) / denom
