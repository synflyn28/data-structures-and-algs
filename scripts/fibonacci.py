"""
Compute n fibonacci numbers using recursion.
"""

def fibonacci(n):
    """
    This function computes the n-th fibonacci number using recursion.
    """
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
