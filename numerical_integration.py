from typing import Callable


def left_riemann_sum(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    h = (b - a)/n
    riemann_sum = 0
    for i in range(n):
        x_i = a + i*h
        riemann_sum += h*f(x_i)
    return riemann_sum
