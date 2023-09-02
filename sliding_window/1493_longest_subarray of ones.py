"""
easy to understand
"""


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        zeropos = -1
        max_size = 0
        l = r = 0
        while l <= r and r < len(nums):

            if nums[r] == 0:
                if zeropos >= l:
                    l = zeropos + 1
                zeropos = r

            _len = r - l

            max_size = max(max_size, _len)
            r += 1

        _len = r - l - 1

        return max(max_size, _len)