"""
https://leetcode.com/problems/delete-operation-for-two-strings/description/

same as edit distance
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(dp)):
            for j in range(len(dp[i])):

                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]

