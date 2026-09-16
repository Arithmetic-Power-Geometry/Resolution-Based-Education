import numpy as np
from benchmarks.oulad_selective_falsification import top_confidence_mask


def test_matched_coverage_selects_requested_fraction():
    p=np.array([.01,.2,.45,.55,.8,.99])
    m=top_confidence_mask(p,.5)
    assert m.sum()==3


def test_matched_coverage_prefers_confident_cases():
    p=np.array([.01,.49,.51,.99])
    m=top_confidence_mask(p,.5)
    assert set(np.where(m)[0])=={0,3}


def test_mask_nonempty_at_tiny_coverage():
    assert top_confidence_mask(np.array([.2,.8]),.01).sum()==1
