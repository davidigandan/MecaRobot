import os
import numpy as np
from numpy.testing import assert_array_almost_equal
from ..get_xy_corrections import get_corrections
import pytest

def test_get_corrections():
    with pytest.raises(ValueError):
        result = get_corrections(30,5)
    
    
