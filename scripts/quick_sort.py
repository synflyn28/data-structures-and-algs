"""
This script implements the quick sort algorithm.
"""

def quick_sort(my_array):
    """
    This function sorts an array using the quick sort algorithm.
    """

    qs_helper(my_array, 0, len(my_array) - 1)

    return my_array


def qs_helper(my_array, start, end):
    """
    This function is a helper function that helps process
    each decomposition of the array in quick sort. 
    """

    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while right >= left:
        if my_array[left] > my_array[pivot] and my_array[right] < my_array[pivot]:
            
            # Swap the pivot with the right element
            my_array[left], my_array[right] = my_array[right], my_array[left]

        elif my_array[left] <= my_array[pivot]:
            left += 1 # Move the left pointer to the right

        elif my_array[right] >= my_array[pivot]:
            right -= 1 # Move the right pointer to the left

    # After swapping move the pivot point to the correct sorted position
    my_array[pivot], my_array[right] = my_array[right], my_array[pivot]

    # Recursively run the helper function on the values that are less than on the left
    # side of the pivot 
    qs_helper(my_array, start, right - 1)

    # Recursively run the helper function on the values that are greater than on the right
    # side of the pivot 
    qs_helper(my_array, right + 1, end)


if __name__ == "__main__":
    my_array = [3, 5, 2, 1, 4, 6, 7, 8, 9]
    print(quick_sort(my_array))