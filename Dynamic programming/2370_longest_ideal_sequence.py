"""
https://leetcode.com/problems/longest-ideal-subsequence/description/
"""


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        mem = {}

        def dfs(i, prev):
            if i == len(s):
                return 0

            if (i, prev) in mem:
                # print("mem used")
                return mem[(i, prev)]

            size1,size2,=0 ,0
            for p in [0, 1]:
                if p == 0:  # exclude
                    size1 = dfs(i + 1, prev)
                else:
                    if prev == "" or abs(ord(prev) - ord(s[i])) <= k:
                        size2 = dfs(i + 1, s[i]) + 1

            c1 = max(size1,size2)
            mem[(i, prev)] = c1
            return c1

        return dfs(0, "")

    # def longestIdealString(self, s: str, k: int) -> int:
    # lis = {}
    # lis[len(s)-1] = [1, 0]
    #
    # for i in range(len(s)-2, -1, -1):
    #     lis[i] = [0, 0]
    #     if abs(ord(s[i]) - ord(s[i+1])) <= k:
    #         lis[i][0] = max(lis[i+1]) + 1
    #     else:
    #         lis[i][1] = lis[i+1][1] + 1
    # print(lis)
    # return max(lis[0])


# print(Solution().longestIdealString("acfgbd", 2))
# print(Solution().longestIdealString("abcd", 3))
# print(Solution().longestIdealString("jxhwaysa", 14))


class Solution:
    def minimumTotal(self, triangle) -> int:

        mem = {}

        def dfs(i, j):
            print(i, j)

            if i == len(triangle):
                return 0

            if (i, j) in mem:
                return mem[(i, j)]

            s = min(
                dfs(i + 1, j),
                dfs(i + 1, j + 1)
            ) + triangle[i][j]

            mem[(i, j)] = s

            return s

        return dfs(0, 0)

print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))