"""
https://leetcode.com/problems/range-sum-query-immutable/
we will use prefix sum approach
Time - O(N) construction
SumRange - O(1)

we can use segment tree but since there are no updates in the array it will be an over kill

"""


class NumArray:

    def __init__(self, nums):

        self.prefix_sum = []
        total = 0
        for i in nums:
            total += i
            self.prefix_sum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left - 1]
