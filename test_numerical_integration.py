from typing import Callable
import numpy as np
from numerical_integration import *

def f(x):
    return 3*(x**2)*np.exp(x**3)

a = 0
b = 1

expected = (np.exp(b**3) - np.exp(a**3))


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
    success =  diff < 0.001
    message = f"Computed integral differs from analytical integral with {diff}"
    assert success, message
    
