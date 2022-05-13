"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
:: two_pointer
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        start = 0
        for i in range(start, len(nums)):
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]

        return start + 1

    def removeDuplicatesAtmostTwo(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        start = 0
        count = 1
        for i in range(start + 1, len(nums)):
            if nums[i] != nums[start]:
                start += 1
                nums[start] = nums[i]
                count = 1
            else:
                count += 1
                if count <= 2:
                    start += 1
                    nums[start] = nums[i]

        print(nums)
        return start + 1


k = Solution().removeDuplicatesAtmostTwo([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4])
print(k)
