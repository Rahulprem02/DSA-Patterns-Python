
# Leetcode 125: https://leetcode.com/problems/valid-palindrome/
# Pattern: Two Pointer Appproch 


import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        n = len(string)

        for i in range(n//2):
            if string[i] != string[n-1-i]:
                return False
        return True

    
        # Time Complexity: O(n)
        # Space Complexity: O(1)  
    
