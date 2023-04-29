"""
https://leetcode.com/problems/longest-increasing-subsequence/

1D dp questions.

every element is LIS of 1 length


"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(0, i):

                if (nums[i] > nums[j] and dp[i] <= dp[j]):
                    dp[i] = dp[j] + 1

        return max(dp)
