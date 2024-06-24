"""
This script implements the binary search algorithm.
"""

def binary_search(array, target):
    """
    Search for an element in a given array using a binary search
    strategy.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = array[middle]

        if target == middle_element:
            return middle
        elif target < middle_element:
            right = middle - 1
        else:
            left = middle + 1
    return -1

if __name__ == "__main__":
    print(binary_search([1, 5, 10, 12, 25, 30, 32], 29))