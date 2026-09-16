import numpy as np
from benchmarks.oulad_burden_bootstrap import paired_bootstrap_saving


def test_bootstrap_detects_positive_saving():
    used=np.array([2.,3.,4.,5.]*50)
    mean,lo,hi,p=paired_bootstrap_saving(used,6.,n_boot=1000,seed=7)
    assert mean>0 and lo>0 and hi>0 and p<.01


def test_zero_saving_not_declared_positive():
    used=np.full(100,6.)
    mean,lo,hi,p=paired_bootstrap_saving(used,6.,n_boot=500,seed=9)
    assert mean==0 and lo==0 and hi==0 and p==1.0


def test_reproducible():
    used=np.array([1.,2.,3.,4.,5.,6.])
    a=paired_bootstrap_saving(used,6.,n_boot=250,seed=11)
    b=paired_bootstrap_saving(used,6.,n_boot=250,seed=11)
    assert a==b
