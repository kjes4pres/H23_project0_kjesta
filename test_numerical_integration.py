from typing import Callable
import numpy as np
from numerical_integration import *
import pytest


def f(x):
    return 3 * (x**2) * np.exp(x**3)


a = 0
b = 1

expected = np.exp(b**3) - np.exp(a**3)


def test_left_riemann_sum():
    n = 4080
    computed = left_riemann_sum(f, a, b, n)
    diff = abs(computed - expected)
    success = diff < 0.001
    message = f"Computed integral differs from analytical integral with {diff}"

    assert success, message


def test_midpoint():
    n = 70
    computed = midpoint(f, a, b, n)
    diff = abs(computed - expected)
    success = diff < 0.001
    message = f"Computed integral differs from analytical integral with {diff}"
    assert success, message


@pytest.mark.parametrize("method, n", [("midpoint", 1000), ("left_riemann_sum", 5000)])
def test_integrate(method, n):
    computed = integrate(f, a, b, n, method)
    diff = abs(computed - expected)
    success = diff < 0.001
    message = f"Computed integral differs from analytical integral with {diff}"

    assert success, message


def test_integrate_raises_ValueError_for_invalid_method():
    with pytest.raises(ValueError):
        n = 5000
        integrate(f, a, b, n, "notmidpoint")
