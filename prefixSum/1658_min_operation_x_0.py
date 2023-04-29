"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

this question converts to prefix sum question find how [ipad]
other dp backtrack + memoize [2^N]

TIme O(N)
space: O(N)

"""


class Solution:
    def minOperations(self, nums, x: int) -> int:
        hash_map = {0:-1}
        prefix_sum = 0
        max_len = 0

        sum_req = sum(nums) - x

        for i in range(0, len(nums)):

            prefix_sum += nums[i]
            diff = prefix_sum - sum_req

            if diff in hash_map:
                max_len = max(max_len, i - hash_map[diff])

            hash_map[prefix_sum] = i

        if max_len == 0:
            return -1
        else:
            return len(nums) - max_len


