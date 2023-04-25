"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""


class Solution:
    def canPartition(self, nums) -> bool:

        if sum(nums) % 2 != 0:
            return False

        dp = [[False] * int((sum(nums) / 2) + 1) for _ in range(0, len(nums) + 1)]

        for i in range(0, len(dp)):
            for j in range(0, len(dp[i])):

                if j == 0:
                    dp[i][j] = True
                elif i == 0 and j != 0:
                    dp[i][j] = False
                else:
                    a = dp[i - 1][j]
                    b = False
                    if j >= nums[i - 1]:
                        b = dp[i - 1][j - nums[i - 1]]
                    dp[i][j] = a or b
        # print(dp)
        return dp[-1][-1]

