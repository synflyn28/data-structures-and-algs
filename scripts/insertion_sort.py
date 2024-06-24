"""
This script contains the implementation of the insertion sort algorithm.

(c) 04/12/2024 Justin Reid
"""

def insertion_sort(arr):
    """
    This function sorts an array using insertion sort.
    """

    for i in range(1, len(arr)):
        key = arr[i]
        last = i - 1

        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last -= 1

        arr[last + 1] = key # Insert key into the correct final position

arr = [29, 10, 14, 37, 14]
insertion_sort(arr)

print(arr)