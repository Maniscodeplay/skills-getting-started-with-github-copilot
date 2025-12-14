"""Additional calculator operations module."""


def factorial(n):
    """Calculate factorial of a number.
    
    Args:
        n: Non-negative integer
        
    Returns:
        The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def square_root(n):
    """Calculate the square root of a number.
    
    Args:
        n: Non-negative number
        
    Returns:
        The square root of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers")
    return n ** 0.5


def percentage(value, percent):
    """Calculate percentage of a value.
    
    Args:
        value: The base value
        percent: The percentage to calculate
        
    Returns:
        The percentage of the value
    """
    return (value * percent) / 100
