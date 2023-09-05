import pytest 
import math as m
import numpy as np

from calculator import *

@pytest.mark.parametrize(
        "x, y, expected", [(1, 2, 3), (2, 2, 4), (1, 1, 2)]
)
def test_add(x, y, expected):
    computed = add(x, y)
    success = computed == expected
    message = f"Computed value was {computed}, expected value was {expected}."
    assert success, message

@pytest.mark.parametrize(
        "x, y, expected", [(2,2,1),(1, 0.5, 2),(0.1, 100, 0.001)]
)
def test_divide(x, y, expected):
    computed = divide(x, y)
    success = computed == expected or m.isclose(expected, computed) == True
    message = f"Computed value was {computed}, expected value was {expected}."
    assert success, message 


@pytest.mark.parametrize(
    "x, expected", [(0,1), (2,2), (5,120)]
)
def test_factorial(x, expected):
    computed = factorial(x)
    success = computed == expected or m.isclose(expected, computed) == True
    message = f"Computed value was {computed}, expected value was {expected}."
    assert success, message


@pytest.mark.parametrize(
        "x, expected", [(0, 0), (np.pi/4, 1/(np.sqrt(2))), (np.pi/2, 1), (3*np.pi/2, -1)]
)
def test_sin(x, expected):
    computed = sin(x)
    success = computed == expected or m.isclose(expected, computed) == True
    message = f"Computed value was {computed}, expected value was {expected}."
    assert success, message


@pytest.mark.parametrize(
    "list, expected", [([1, 2, 3], 2), ([0.5, 0.5], 0.5), ([3, 4, 5, 8], 5)]
)
def test_mean(list, expected):
    computed = mean(list)
    success = computed == expected or m.isclose(expected, computed) == True
    message = f"Computed value was {computed}, expected value was {expected}."
    assert success, message


@pytest.mark.parametrize(
    "list, expected", [([1,2,3], 2/3), ([1,1,1,1], 0), ([5,10], 6.25)]
)
def test_var(list, expected):
    computed = var(list)
    success = computed == expected or m.isclose(expected, computed) == True
    message = f"Computed value was {computed}, expected value was {expected}."
    assert success, message