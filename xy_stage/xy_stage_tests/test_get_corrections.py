import os
import numpy as np
from numpy.testing import assert_array_almost_equal
from ..get_xy_corrections import get_corrections
import pytest

def test_get_corrections():
        result = get_corrections(30,5)
        expect = np.array([[5.0000000e+00],[4.1948373e-17]])
        assert_array_almost_equal(result, expect, decimal=4)
    
    
