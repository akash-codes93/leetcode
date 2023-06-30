"""
https://leetcode.com/problems/contiguous-array/description/
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

replace 0 with -1
and now question becomes find largest array with sum 0
"""


class Solution:
    def findMaxLength(self, nums) -> int:
        nums = [-1 if i == 0 else i for i in nums]
        prefix_sum = {0: -1}

        max_len = 0
        total = 0
        for idx, i in enumerate(nums):
            total += i
            if total in prefix_sum:
                max_len = max(max_len, idx - prefix_sum[total])
            else:
                prefix_sum[total] = idx

        return max_len