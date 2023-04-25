"""
https://leetcode.com/problems/coin-change/
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [[float('inf')] * (amount + 1) for i in range(0, len(coins) + 1)]

        for i in range(0, len(dp)):
            for j in range(0, len(dp[i])):

                if j == 0:
                    dp[i][j] = 0
                else:
                    exc = dp[i - 1][j]
                    inc = float('inf')

                    if (j >= coins[i - 1]):
                        inc = 1 + dp[i][j - coins[i - 1]]
                    dp[i][j] = min(exc, inc)

        if dp[-1][-1] == float('inf'):
            return -1

        return dp[-1][-1]