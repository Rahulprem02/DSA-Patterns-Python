
# Leetcode 455: https://leetcode.com/problems/assign-cookies/
# Pattern: Two Pointer Appproch

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()
        i,j,count = 0,0,0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
            #if s[j] == g[i]:
                count += 1
                i += 1
            j += 1
            # elif s[j] < g[i]:
            #     i += 1
            # else:
            #     continue
        
        return count
    
    # Time Complexity: O(n + m) length of list s, g
    # Space Complexity: O(1)
            



        