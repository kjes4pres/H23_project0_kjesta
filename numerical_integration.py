from typing import Callable

def left_riemann_sum(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    h = (b - a)/n
    riemann_sum = 0
    for i in range(n):
        x_i = a + i*h
        riemann_sum += h*f(x_i)
    return riemann_sum


def midpoint(f: Callable[[float], float], a: float, b: float, n: int) -> float:

    if not isinstance(n, int) or n <= 0:
        raise ValueError(f"n must be an integer and bigger than zero, not {n}.")
    if b <= a:
        raise ValueError("The upper limit (b) must be greater than the lower limit (a).")

    h = (b - a)/n
    midpoint_result = 0
    for i in range(n):
        x_i = a + i*h
        midpoint_result += (h/2)*(f(x_i) + f(x_i + h))
    return midpoint_result


def integrate(
    f: Callable[[float], float], a: float, b: float, n: int, method: str = "midpoint"
) -> float:
    
    if method not in ["midpoint", "left_riemann_sum"]:
        raise ValueError("Only methods allowed is midpoint or left_riemann_sum.")
        
    if method == "midpoint":
        return midpoint(f, a, b, n)
    else:
        return left_riemann_sum(f, a, b, n)