"""
https://leetcode.com/problems/is-subsequence/
:: two_pointer  = O(s+t)

DP approach: Find LCS between the two string is length of len(LCS) == len(s) return True else False
but time complexity is O(s.t)
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        s_index = 0
        for i in t:
            if i == s[s_index]:
                s_index += 1

            if s_index >= len(s):
                break

        if s_index == len(s):
            return True

        return False


class SolutionDP:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0] * (len(s)+1) for _ in range(0, len(t) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                print(t, i, s, j)
                if t[i-1] == s[j-1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp)
        if len(s) == dp[-1][-1]:
            return True
        else:
            return False


p = SolutionDP().isSubsequence(s="bg", t="ahbgdc1")
print(p)
