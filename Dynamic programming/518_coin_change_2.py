"""
https://leetcode.com/problems/coin-change-ii/description/

unbounded kanpsack

repeatiting subproblem
optimal substructure


"""


class Solution:
    def change(self, amount: int, coins) -> int:

        dp = [[0] * (amount + 1) for _ in range(0, len(coins) + 1)]

        dp[0][0] = 1

        for i in range(1, len(dp)):

            for j in range(0, len(dp[i])):

                if j == 0:
                    dp[i][j] = 1
                else:
                    a = dp[i - 1][j]
                    b = 0
                    if j >= coins[i - 1]:
                        b = dp[i][j - coins[i - 1]]

                    dp[i][j] = a + b

        return dp[-1][-1]
