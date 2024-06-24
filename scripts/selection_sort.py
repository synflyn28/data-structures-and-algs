"""
This script implements the selection sort algorithm.

(c) 4/12/2024 Justin Lynn Reid
"""

def selection_sort(arr):
   for i in range(len(arr)):
      min_x = i

      for item in range(i + 1, len(arr)):
         if arr[item] < arr[min_x]:
            min_x = item
      # Swap the beginning "min" value with the actual min value
      # gathered from the inner loop      
      arr[i], arr[min_x] = arr[min_x], arr[i]
   
arr = [20, 12, 10, 15, 2]
selection_sort(arr)

print(arr)