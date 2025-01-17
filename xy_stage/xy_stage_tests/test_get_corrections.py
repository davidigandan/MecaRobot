import os
import numpy as np
from numpy.testing import assert_array_almost_equal
from ..get_xy_corrections import get_corrections
import pytest


@pytest.mark.parametrize(
    "angle, error_magnitude, expected",
    [
        (30, 5, np.array([[5.0000000e00], [4.1948373e-17]])),
    ],
)
def test_get_corrections(angle, error_magnitude, expected):
    result = get_corrections(angle, error_magnitude)

    assert_array_almost_equal(result, expected, decimal=7)