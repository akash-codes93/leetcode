"""
https://leetcode.com/problems/longest-common-subsequence/description/

task to find that string


"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0] * (len(text2) + 1) for i in range(0, len(text1) + 1)]

        for i in range(1, len(dp)):

            for j in range(1, len(dp[0])):

                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]