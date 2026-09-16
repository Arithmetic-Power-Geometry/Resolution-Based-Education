from rbe.core import Intervention
from rbe.policy import optimal_resolution_policy


def test_two_stage_policy_resolves_when_no_single_probe_does():
    worlds = ("w1", "w2", "w3", "w4")
    certification = {"w1": 1, "w2": 1, "w3": 0, "w4": 0}

    # Neither probe is a full separator by itself.  After p1, the singleton
    # negative branch is resolved and p2 is needed only on the remaining
    # three-world branch.  Under equal prior mass the expected burden is
    # 1 + (3/4)*1 = 1.75.
    p1 = Intervention(
        "p1",
        cost=1.0,
        leakage=0.0,
        observations={"w1": "a", "w2": "a", "w3": "b", "w4": "a"},
    )
    p2 = Intervention(
        "p2",
        cost=1.0,
        leakage=0.0,
        observations={"w1": "x", "w2": "x", "w3": "x", "w4": "y"},
    )

    result = optimal_resolution_policy(worlds, certification, [p1, p2])
    assert result.resolved
    # Both symmetric first choices have expected burden 1.75; deterministic
    # tie-breaking selects p1.
    assert result.first_probe == "p1"
    assert abs(result.expected_burden - 1.75) < 1e-12


def test_policy_reports_infeasible_when_no_probe_can_resolve():
    worlds = ("w1", "w2")
    certification = {"w1": 1, "w2": 0}
    p = Intervention("same", 1.0, 0.0, {"w1": "z", "w2": "z"})
    result = optimal_resolution_policy(worlds, certification, [p])
    assert not result.resolved
