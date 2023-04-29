"""
scs = s1 +s2 -lcs
"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        # making lcs table
        dp = [[0] * (len(str2) + 1) for _ in range(0, len(str1) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):

                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs = ""

        i = len(dp) - 1
        j = len(dp[0]) - 1

        while i > 0 and j > 0:

            if dp[i - 1][j - 1] < dp[i][j] and dp[i - 1][j - 1] >= dp[i][j - 1] and dp[i - 1][j - 1] >= dp[i - 1][j]:
                lcs += str1[i - 1]
                i -= 1
                j -= 1
            else:

                if dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1

                else:
                    j -= 1

        lcs = lcs[::-1]

        p1 = 0
        p2 = 0
        p3 = 0
        scs = ""

        while p3 < len(lcs):
            print(scs)
            print(lcs, p3)
            print(str1, p1)
            print(str2, p2)
            if lcs[p3] == str1[p1] and lcs[p3] == str2[p2]:
                scs += str1[p1]
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if lcs[p3] != str1[p1]:
                    scs += str1[p1]
                    p1 += 1

                if lcs[p3] != str2[p2]:
                    scs += str2[p2]
                    p2 += 1

        while p1 < len(str1):
            scs += str1[p1]
            p1 += 1

        while p2 < len(str2):
            scs += str2[p2]
            p2 += 1

        print(scs)
        return scs


Solution().shortestCommonSupersequence(str1 = "abac", str2 = "cab")
