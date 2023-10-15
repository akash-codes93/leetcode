"""
https://leetcode.com/problems/max-dot-product-of-two-subsequences/
"""

from typing import List



class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        mem = {}
        arr1 = []
        arr2 = []

        def dotproduct():
            sum = 0
            for k in range(len(arr1)):
                sum += (arr1[k] * arr2[k])
            return sum

        def dfs(i, k1, j, k2):

            if i == len(nums1) or j == len(nums2):
                if k1 == k2:
                    return dotproduct()

                return float('-inf')

            if (i, k1, j, k2) in mem:
                return mem[(i, k1, j, k2)]

            max_sum = float('-inf')

            # option1
            arr1.append(nums1[i])
            arr2.append(nums2[j])
            max_sum = max(max_sum, dfs(i + 1, k1 + 1, j + 1, k2 + 1))
            arr1.pop()
            arr2.pop()

            # option2
            arr1.append(nums1[i])
            max_sum = max(max_sum, dfs(i + 1, k1 + 1, j + 1, k2))
            arr1.pop()

            # option3
            arr2.append(nums2[i])
            max_sum = max(max_sum, dfs(i + 1, k1, j + 1, k2 + 1))
            arr2.pop()

            # option 4
            max_sum = max(max_sum, dfs(i + 1, k1, j + 1, k2))

            mem[(i, k1, j, k2)] = max_sum
            return max_sum

        return dfs(0,0,0,0)