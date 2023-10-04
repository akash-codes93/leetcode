"""
extended moore algorithm
https://leetcode.com/problems/majority-element-ii/
"""
from typing import List


class Solution:
    def majorityElement(self, nums):
        num1 = None
        num2 = None

        c1 = 0
        c2 = 0

        for n in nums:

            if n == num1:
                c1 += 1

            elif n == num2:
                c2 += 1

            elif c1 == 0:
                num1 = n
                c1 = 1
            elif c2 == 0:
                num2 = n
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1

        output = []
        if num1 is not None:
            count = 0
            for n in nums:
                if n == num1:
                    count += 1
            if count > len(nums) // 3:
                output.append(num1)

        if num2 is not None:
            count = 0
            for n in nums:
                if n == num2:
                    count += 1
            if count > len(nums) // 3:
                output.append(num2)

        return output


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        i = i
        found = True
        # monotonic increasing
        while i < len(nums):
            if nums[i] <= nums[i-1]:
                found = False
            i += 1

        if found:
            return True

        found = True
        while i < len(nums):
            if nums[i] >= nums[i-1]:
                found = False
            i += 1
        if found:
            return True

        return False
































