def add(x: float, y: float) -> float:
    '''Addition of two floats.'''
    return x + y


def divide(x: float, y: float) -> float:
    '''Divison of two floats'''
    return x/y


def factorial(x: float) -> float:
    '''Take factorial of a number, ex.: 5! = 1*2*3*4*5 = 120'''
    counter = 1
    factorial_result = 1
    while counter <= x:
        factorial_result = factorial_result*counter
        counter = counter + 1
    return factorial_result


def sin(x: float) -> float:
    '''Calculate sin(x) using  the truncated Taylor series expansion'''
    N = 20
    result = 0
    for n in range(N + 1):
        result += (((-1)**n)*x**(2*n + 1))/factorial(2*n + 1)
    return result


def mean(x: list) -> float:
    '''Calculate the mean value of a list of numbers'''

