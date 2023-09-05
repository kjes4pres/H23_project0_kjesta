import pytest 

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
    "x, expected", [(0,1), (2,1), (5,120)]
)
def test_factorial(x, expected):
    computed = factorial(x)
    success = computed == expected or m.isclose(expected, computed) == True
    message = f"Computed value was {computed}, expected value was {expected}."
    assert success, message


@pytest.mark.parametrize(
)
def test_sin():
    computed = sin()