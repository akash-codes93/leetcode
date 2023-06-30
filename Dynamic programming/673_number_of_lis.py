"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
"""


class SolutionBT:
    """
    Gives TLE
    """

    def findNumberOfLIS(self, nums) -> int:
        max_size = [0]
        max_size_count = [0]

        def dfs(i, size):
            if size > max_size[0]:
                max_size[0] = size
                max_size_count[0] = 1
            elif size == max_size[0]:
                max_size_count[0] += 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    size += 1
                    dfs(j, size)
                    size -= 1

        for k in range(0, len(nums)):
            dfs(k, 1)
            # print(k, size)

        return max_size_count[0]


class Solution:
    def findNumberOfLIS(self, nums) -> int:
        dp = {}
        lis, global_count = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            max_len, max_cnt = 1, 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:

                    length, count = dp[j]
                    if length + 1 > max_len:
                        max_len = length + 1
                        max_cnt = count
                    elif length + 1 == max_len:
                        max_cnt += count

            if max_len > lis:
                lis, global_count = max_len, max_cnt
            elif max_len == lis:
                global_count += max_cnt

            dp[i] = [max_len, max_cnt]
        return global_count

