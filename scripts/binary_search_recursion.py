"""
This module contains the binary search algorithm implemented using recursion.

(c) 4/8/2024 Justin Lynn Reid
"""

def binary_search(my_array, target):
    """
    This function implements the binary search algorithm using recursion.
    """
    left = 0
    right = len(my_array) - 1
    result = helper(my_array, target, left, right)

    return result


def helper(my_array, target, left, right):
    """
    This function is a helper function for the binary_search function.
    """

    if left > right:
        return -1
    
    middle = (left + right) // 2
    middle_element = my_array[middle]

    if target == middle_element:
        return middle
    elif target < middle_element:
        right = middle - 1
        return helper(my_array, target, left, right)
    else:
        left = middle + 1
        return helper(my_array, target, left, right)