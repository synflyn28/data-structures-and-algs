"""
This script contains code that reverses a string using O(n) time complexity 
and O(1) space complexity.
"""

class Solution:
    def reverse_string(self, s: str) -> str:
        """
        Reverses a string using O(n) time complexity and O(1) space complexity.
        """

        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
            