"""
https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        needs = {}

        for i in range(0, len(nums)):
            i_needs = target - nums[i]
            try:
                output.append(needs[i_needs])
                output.append(i)
                break
            except KeyError:
                needs[nums[i]] = i

        return output


print(Solution().twoSum([3, 3], 6))
