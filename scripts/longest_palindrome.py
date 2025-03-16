"""
This script contains the implementation for finding the longest palindrome in a string.
"""

class Solution:
    def longest_palindrome(self, s: str) -> str:
        """
        Finds the longest palindrome in a string.
        """

        result = ""

        for i in range(len(s)):
            word1 = self.check_palindrome(s, i, i)
            word2 = self.check_palindrome(s, i, i + 1) # Additional character checked for even case

            if len(word1) >= len(word2):
                longest = word1
            else:
                longest = word2

            if len(longest) > len(result):
                result = longest

        return result

    
    def check_palindrome(self, s, left, right):
        """
        Checks if a substring is a palindrome.
        """

        # Move pointers if strings are equal and pointer indexes are within bounds 
        # of input string length
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left + 1: right] # Return substring smaller than what is checked in while because loop always overshoots the substring