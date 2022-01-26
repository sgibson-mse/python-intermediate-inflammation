"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_max_floats():
    """Test that max function works for array of floats"""
    from inflammation.models import daily_max

    test_input = np.array([[1.0, 100.0],
                           [99.9, 47.7],
                           [69.3, 31.1]])

    test_result = np.array([99.9, 100.0])

    npt.assert_array_equal(daily_max(test_input), test_result)


def test_daily_min_integers():
    """Test that max function works for array of positive and negative integers"""
    from inflammation.models import daily_min

    test_input = np.array([[1, 100],
                           [99, -47],
                           [69, 31]])

    test_result = np.array([1, -47])

    npt.assert_array_equal(daily_min(test_input), test_result)


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])