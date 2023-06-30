"""
https://leetcode.com/problems/range-sum-query-immutable/

303
we will use prefix sum approach
Time - O(N) construction
SumRange - O(1)

we can use segment tree but since there are no updates in the array it will be an over kill

307
we will use a segment tree as updates are frequent [above method can also be used but updates would take
O(N) as prefix sum array needs to be reconstructed]
Time - O(N)
Sumrange - log(N)
update - log(N)

"""
import math


class NumArrayImmutable:

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


class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)

        # height of tree
        height = math.ceil(math.log2(self.n + 1))

        # Maximum size of segment tree
        max_size = 2 * (2 ** height - 1)

        # Allocate memory
        self.st = [0] * max_size
        self.construct_segment_tree(0, 0, self.n - 1)

    def construct_segment_tree(self, si, l, r):
        if l == r:
            self.st[si] = self.nums[l]
            return self.nums[l]

        mid = (l + r) // 2
        self.st[si] = self.construct_segment_tree((2 * si) + 1, l, mid) + self.construct_segment_tree((2 * si) + 2,
                                                                                                      mid + 1, r)
        return self.st[si]

    def update_st(self, si, sl, sr, pos, diff):
        if pos < sl or pos > sr:
            return

        self.st[si] += diff

        # not leaf node
        if sl != sr:
            mid = (sl + sr) // 2
            self.update_st((2 * si) + 1, sl, mid, pos, diff)
            self.update_st((2 * si) + 2, mid + 1, sr, pos, diff)

    def update_st_better(self, si, sl, sr, pos, val):

        if pos < sl or pos > sr:
            return self.st[si]

        if sl == sr:
            self.st[si] = val
            return val

        mid = (sl + sr) // 2
        self.st[mid] = self.update_st_better((2 * si) + 1, sl, mid, pos, val) + self.update_st_better(
            (2 * si) + 2, mid + 1, sr, pos, val)
        return self.st[mid]

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.update_st(0, 0, self.n - 1, index, diff)
        # self.update_st_better(0, 0, self.n-1, index, value)

    def get_sum(self, si, sl, sr, l, r):

        # total overlap
        if l <= sl and r >= sr:
            return self.st[si]

        # no overlap
        if sr < l or sl > r:
            return 0

        # partial overlap
        mid = (sl + sr) // 2
        return self.get_sum((2 * si) + 1, sl, mid, l, r) + self.get_sum((2 * si) + 2, mid + 1, sr, l, r)

    def sumRange(self, left: int, right: int) -> int:
        return self.get_sum(0, 0, self.n - 1, left, right)
