def add(x: float, y: float) -> float:
    '''Addition of two floats.'''
    return x + y

def divide(x: float, y: float) -> float:
    '''Divison of two floats'''
    return x/y


def factorial(x:float) -> float:
    '''Take factorial of a number, ex.: 5! = 1*2*3*4*5 = 120'''
    counter = 1
    factorial_result = 1
    while counter <= x:
        factorial_result = factorial_result*counter
        counter = counter + 1
    return factorial_result

