"""
https://leetcode.com/problems/is-subsequence/
:: two_pointer
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


p = Solution().isSubsequence(s="", t="ahbgdc1")
print(p)
