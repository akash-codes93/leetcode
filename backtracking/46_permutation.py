"""
https://leetcode.com/problems/permutations/
similar to anagrams swapping will be used.
"""

import copy


class Solution:
    def permute(self, nums):

        main_output = []

        def looper(i):
            if i == len(nums) - 1:
                main_output.append(copy.copy(nums))

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                looper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        looper(0)
        return main_output

    def permuteUnique(self, nums):
        main_output = []

        def looper(i):
            if i == len(nums) - 1:
                main_output.append(copy.copy(nums))

            for j in range(i, len(nums)):
                if i != j and nums[i] == nums[j]:
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                looper(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        looper(0)
        return main_output


a = Solution().permuteUnique([2, 2, 1, 1])
print(a)

# [2,2,1,1]
