from rbe.attainment import LearnerRCOResult, RBEState, course_metrics, weighted_programme_metric


def test_positive_resolution_required_for_rca():
    ar = LearnerRCOResult(82, 60, 0.05, 0.10, True, burden=1.0)
    rn = LearnerRCOResult(82, 60, 0.05, 0.10, False, burden=2.0)
    assert ar.rca == 1 and ar.state == RBEState.AR
    assert rn.rca == 0 and rn.state == RBEState.RN


def test_unresolved_and_not_attained_states():
    au = LearnerRCOResult(82, 60, 0.30, 0.10, None)
    na = LearnerRCOResult(50, 60, 0.05, 0.10, True)
    assert au.state == RBEState.AU
    assert na.state == RBEState.NA


def test_course_metrics_preserve_rn_and_unresolved():
    records = [
        LearnerRCOResult(82, 60, 0.05, 0.10, True, burden=1.0),
        LearnerRCOResult(82, 60, 0.25, 0.10, None, burden=2.0),
        LearnerRCOResult(82, 60, 0.05, 0.10, False, burden=3.0),
        LearnerRCOResult(50, 60, 0.05, 0.10, True, burden=0.0),
    ]
    m = course_metrics(records)
    assert m["PAR"] == 0.75
    assert m["RR"] == 0.75
    assert m["RAR"] == 0.25
    assert m["UAR"] == 0.25
    assert m["RNR"] == 0.25
    assert m["MRB"] == 1.5


def test_weighted_programme_metric():
    value = weighted_programme_metric([0.6, 0.8], [1, 3])
    assert abs(value - 0.75) < 1e-12
