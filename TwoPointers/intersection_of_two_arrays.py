

# Leetcode 349:   https://leetcode.com/problems/intersection-of-two-arrays/
# Pattern: Two Pointer Appproch 

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result = set()
        while i < len(nums1)  and j < len(nums2):

            if nums1[i] < nums2[j]:
                i +=1
            elif nums1[i] > nums2[j]:
                j +=1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        return list(result)
    

        # Time Complexity: O(n log n + m log m)
        # Space Complexity: O(1)
    

#  Brute Force Approach 

    
#class Solution:
 #   def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # x = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             if nums1[i] in x:
        #                 continue
        #             else:
        #                 x.append(nums1[i])
        # return x


        # Time Complexity: 	O(n * m)
        # Space Complexity: O(1)