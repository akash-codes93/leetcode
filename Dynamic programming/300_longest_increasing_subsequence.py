"""
https://leetcode.com/problems/longest-increasing-subsequence/

1D dp questions.

every element is LIS of 1 length
O(n2)

"""

import bisect
from typing import List

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#
#         dp = [1] * len(nums)
#
#         for i in range(1, len(nums)):
#             for j in range(0, i):
#
#                 if nums[i] > nums[j] and dp[i] <= dp[j]:
#                     dp[i] = dp[j] + 1
#
#         return max(dp)


"""
O(nlogn)
"""


class Solution:
    def lengthOfLIS(self, nums) -> int:

        dp = []
        # cp has nothing to do with this algo it is for checking purpose that
        # cp stores max len of sequence to that point.
        cp = [1] * len(nums)
        max_len = 0

        for i in range(len(nums)):
            elem = nums[i]

            idx = bisect.bisect_left(dp, elem)

            if idx == len(dp):
                dp.append(elem)
            else:
                dp[idx] = elem

            cp[i] = idx + 1

            if idx + 1 > max_len:
                max_len = len(dp)

        print(cp)
        print(dp)
        return max_len


# print(Solution().lengthOfLIS([1, 2, -1, 3, 2]))
print(Solution().lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14,
                              1, 9, 5, 13, 3, 11, 7, 15]))
