# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Licensed under the Apache License, Version 2.0.
"""Resolution-Based Education (RBE) v1.0 reference implementation.

Six layers: curriculum, pedagogy, learning, assessment, certification, feedback.
This module is intentionally dependency-free so the formal kernel is auditable.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Mapping, Sequence, Tuple


@dataclass(frozen=True)
class RCO:
    """Resolvable Capability Outcome: (capability, environments, perturbations, decision)."""
    id: str
    capability: str
    environments: Tuple[str, ...]
    perturbations: Tuple[str, ...]
    pass_threshold: float = 0.60


@dataclass(frozen=True)
class LearnerWorld:
    id: str
    capabilities: Mapping[str, float]
    certify: bool


@dataclass(frozen=True)
class Probe:
    id: str
    capability: str
    threshold: float
    cost: float
    leakage: float
    kind: str

    def observe(self, world: LearnerWorld) -> str:
        return "pass" if world.capabilities.get(self.capability, 0.0) >= self.threshold else "fail"

    def objective(self, leakage_weight: float = 1.0) -> float:
        return self.cost + leakage_weight * self.leakage


@dataclass
class ResolutionEpisode:
    rco_id: str
    production_evidence: str
    probes: List[str] = field(default_factory=list)
    observations: List[str] = field(default_factory=list)
    resolved: bool = False
    decision: bool | None = None
    total_cost: float = 0.0
    total_leakage: float = 0.0


@dataclass
class LedgerEntry:
    learner_id: str
    rco_id: str
    evidence_type: str
    evidence: str
    perturbations: List[str]
    observations: List[str]
    resolved: bool
    decision: bool | None
    burden: float
    leakage: float


def compatible_worlds(worlds: Sequence[LearnerWorld], history: Sequence[Tuple[Probe, str]]) -> List[LearnerWorld]:
    return [w for w in worlds if all(p.observe(w) == obs for p, obs in history)]


def certification_resolved(worlds: Sequence[LearnerWorld]) -> bool:
    return bool(worlds) and len({w.certify for w in worlds}) == 1


def carg(worlds: Sequence[LearnerWorld]) -> bool:
    """A CARG exists when compatible worlds require different certification decisions."""
    return bool(worlds) and not certification_resolved(worlds)


def decision_pairs(worlds: Sequence[LearnerWorld]) -> List[Tuple[str, str]]:
    return [(a.id, b.id) for i, a in enumerate(worlds) for b in worlds[i + 1:] if a.certify != b.certify]


def probe_separates(probe: Probe, a: LearnerWorld, b: LearnerWorld) -> bool:
    return probe.observe(a) != probe.observe(b)


def choose_mrrp(worlds: Sequence[LearnerWorld], probes: Sequence[Probe], used: set[str] | None = None,
                leakage_weight: float = 1.0) -> Probe | None:
    """Greedy MRRP: maximize decision-relevant pair separation per burden+leakage."""
    used = used or set()
    pairs = [(a, b) for i, a in enumerate(worlds) for b in worlds[i + 1:] if a.certify != b.certify]
    if not pairs:
        return None
    candidates = []
    for p in probes:
        if p.id in used:
            continue
        separated = sum(probe_separates(p, a, b) for a, b in pairs)
        if separated:
            objective = max(p.objective(leakage_weight), 1e-12)
            candidates.append((separated / objective, separated, -objective, p.id, p))
    return max(candidates)[-1] if candidates else None


def run_resolution_episode(learner: LearnerWorld, worlds: Sequence[LearnerWorld], probes: Sequence[Probe],
                           rco: RCO, production_evidence: str = "artifact-observed",
                           leakage_weight: float = 1.0, max_probes: int = 10) -> ResolutionEpisode:
    """Adaptive, variable-length certification episode with an explicit stopping rule."""
    history: List[Tuple[Probe, str]] = []
    episode = ResolutionEpisode(rco.id, production_evidence)
    for _ in range(max_probes + 1):
        compatible = compatible_worlds(worlds, history)
        if certification_resolved(compatible):
            episode.resolved = True
            episode.decision = compatible[0].certify
            return episode
        probe = choose_mrrp(compatible, probes, {p.id for p, _ in history}, leakage_weight)
        if probe is None or len(history) >= max_probes:
            return episode
        obs = probe.observe(learner)
        history.append((probe, obs))
        episode.probes.append(probe.id)
        episode.observations.append(obs)
        episode.total_cost += probe.cost
        episode.total_leakage += probe.leakage
    return episode


def capability_passport(learner_id: str, entries: Sequence[LedgerEntry]) -> Dict[str, str]:
    """Feedback layer: convert resolved certification evidence into an auditable passport."""
    result: Dict[str, str] = {}
    for e in entries:
        if e.learner_id != learner_id:
            continue
        result[e.rco_id] = "Resolved-Pass" if e.resolved and e.decision else ("Resolved-Developing" if e.resolved else "Unresolved")
    return result


def ccvrt_cycle() -> Tuple[str, ...]:
    """Pedagogy layer."""
    return ("Construct", "Challenge", "Verify", "Revise", "Transfer")
