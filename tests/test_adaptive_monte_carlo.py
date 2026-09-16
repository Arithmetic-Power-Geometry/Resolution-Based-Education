# Copyright (C) 2026 Mohammad Amir Khusru Akhtar
# Apache-2.0
from benchmarks.adaptive_monte_carlo import simulate

def by_name(): return {r['protocol']:r for r in simulate(n=20000,seed=20260916,threshold=.90)}

def test_adaptive_rbe_resolves_more_than_fixed_protocols():
    r=by_name(); assert r['adaptive_rbe']['resolved_rate']>r['fixed_targeted']['resolved_rate']>r['fixed_viva']['resolved_rate']

def test_adaptive_rbe_costs_far_less_than_generic_viva():
    r=by_name(); assert r['adaptive_rbe']['mean_burden']<0.5*r['fixed_viva']['mean_burden']

def test_adaptive_stopping_uses_fewer_probes_than_fixed_targeted():
    r=by_name(); assert r['adaptive_rbe']['mean_probes']<r['fixed_targeted']['mean_probes']

def test_no_false_superiority_claim_on_error():
    # Important falsification guard: in this declared synthetic model adaptive
    # RBE resolves many more cases but does NOT have the lowest resolved-case
    # error. The repository must preserve this tradeoff rather than hide it.
    r=by_name(); assert r['adaptive_rbe']['decision_error_rate_resolved']>r['fixed_targeted']['decision_error_rate_resolved']
