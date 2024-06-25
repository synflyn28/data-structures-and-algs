"""
This script implements the quick sort algorithm.
"""

def quick_sort(my_arr):
    """
    Sorts an array using the quick sort algorithm.
    """

    qshelper(my_arr, 0, len(my_arr) - 1)
    return my_arr
    
def qshelper(my_arr, start, end):
    """
    Helper function for quick_sort.
    """

    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while right >= left:
        if my_arr[left] > my_arr[pivot] and my_arr[right] < my_arr[pivot]:
            my_arr[left], my_arr[right] = my_arr[right], my_arr[left]
        elif my_arr[left] <= my_arr[pivot]:
            left += 1
        elif my_arr[right] >= my_arr[pivot]:
            right -= 1

    my_arr[pivot], my_arr[right] = my_arr[right], my_arr[pivot]

    qshelper(my_arr, start, right - 1)
    qshelper(my_arr, right + 1, end)