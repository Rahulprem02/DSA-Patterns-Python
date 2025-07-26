
# Leetcode 28: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Pattern: Two Pointer Appproch 


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
    
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
    

    #  Brute Force Approach 
    #  Not pass on all test cases.

    # class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:

    #     j =0
    #     if needle in haystack:
    #         for i in range(len(haystack)):
    #             if needle[j] == haystack[i]:
    #                 j +=1
    #                 if j == len(needle):
    #                     return i+1 - len(needle)
    #             else:
    #                 j = 0
    #     else:
    #         return -1

