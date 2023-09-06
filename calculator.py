def add(x: float, y: float) -> float:
    '''Addition of two floats.'''
    return x + y


def divide(x: float, y: float) -> float:
    '''Divison of two floats'''
    return x/y


def factorial(x: int) -> float:
    '''Take factorial of a  non-negative integer, ex.: 5! = 1*2*3*4*5 = 120.
    '''
    try:
        if x < 0:
            raise ValueError("You can only take factorial of a positive number.")
    except ValueError:
       raise ValueError 
    
    try:
        float == type(x)
    except TypeError:
        print("This function only takes the factorial of integers.")

    counter = 1
    factorial_result = 1
    while counter <= x:
        factorial_result = factorial_result*counter
        counter = counter + 1
    return factorial_result


def sin(x: float) -> float:
    '''Calculate sin(x) using  the truncated Taylor series expansion.'''
    N = 20
    result = 0
    for n in range(N + 1):
        result += (((-1)**n)*x**(2*n + 1))/factorial(2*n + 1)
    return result


def mean(x: list) -> float:
    '''Calculate the mean value of a list of numbers.'''
    length = len(x)
    sum_of_list = 0  
    for i in range(length):
        sum_of_list += x[i]
    mean_value = sum_of_list/length
    return mean_value 


def var(x: list) -> float:
    '''Calculate sample variance of list of numbers.'''
    length = len(x)
    mean_value = mean(x)
    sum = 0  # dummy variable to store sum part of the equation.
    for i in range(length):
        sum += (x[i] - mean_value)**2
    sample_variance = sum/length
    return sample_variance



