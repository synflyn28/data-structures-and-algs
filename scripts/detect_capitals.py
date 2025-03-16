"""
This script detects correct use of capital letters in a string.
"""

class Solution:
    def detect_capital_use(self, word: str) -> bool:
        """
        Detects correct use of capital letters in a string.
        """

        count = 0
        length = len(word)

        for i in range(length):
            if word[i] >= chr(65) and word[i] < chr(91): # Check for uppercase letters using ASCII value conversion
                count += 1

        if count == length:
            return True
        elif count == 0:
            return True
        elif count == 1 and word[0] >= chr(65) and word[0] < chr(91):
            return True
        else:
            return False