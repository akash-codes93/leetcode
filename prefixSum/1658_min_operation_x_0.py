"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

this question converts to prefix sum question find how [ipad]
other dp backtrack + memoize [2^N]

Time O(N)
space: O(N)

"""


class SolutionPrefixSum:
    def minOperations(self, nums, x: int) -> int:
        hash_map = {0: -1}
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


"""
calculate left sum and right sum
for every right sum (l) find right sum (r)
such that l + r = x
"""

from bisect import bisect_left


class SolutionBinarySearchSlidingWindow:

    def minOperations(self, nums, x: int) -> int:

        n = len(nums)
        left, right = [0], [0]

        for i in range(n):
            left.append(left[-1] + nums[i])
            right.append(right[-1] + nums[n - 1 - i])

        res = n + 1
        for idx, num in enumerate(left):
            if num > x: break
            r = x - num
            r_idx = bisect_left(right, r)
            if r_idx < n and right[r_idx] == r:
                res = min(res, idx + r_idx)

        return -1 if res == n + 1 else res