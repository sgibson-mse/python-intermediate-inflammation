"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

#A fixture
#Mark capability adds metadata to the specific test -
@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers"""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1.0, 100], [99.9, 47.7], [69.3, 31.1]], [99.9, 100.0]),
        ([[1, 100], [99, -47], [69, 31]], [99, 100]),
    ])
def test_daily_max(test, expected):
    """Test that max function works for mix of floats and negative numbers"""
    from inflammation.models import daily_max

    npt.assert_array_equal(daily_max(test), expected)

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1.0, 100], [99.9, 47.7], [69.3, 31.1]], [1.0, 31.1]),
        ([[1, 100], [99, -47], [69, 31]], [1, -47]),
    ])
def test_daily_min(test, expected):
    """Test that max function works for mix of floats and negative numbers"""
    from inflammation.models import daily_min

    npt.assert_array_equal(daily_min(test), expected)

def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])