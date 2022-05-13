"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrentMy(self, nums: List[int]) -> List[int]:

        marker = {}
        output = []
        old_nums = nums
        nums = sorted(old_nums, reverse=True)
        print(nums)
        nums_len = len(nums)

        for i in range(nums_len):
            if nums[i] not in marker:
                marker[nums[i]] = [i, i]
            else:
                min_index = marker[nums[i]][0]
                max_index = marker[nums[i]][1]

                if i < min_index:
                    marker[nums[i]][0] = i

                if i > max_index:
                    marker[nums[i]][1] = i

        print(marker)

        for i in range(nums_len):
            output.append(
                nums_len - marker[old_nums[i]][1] - 1
            )

        return output

    def _find_max_element(self, nums):
        _max = nums[0]

        for i in range(len(nums)):
            if _max < nums[i]:
                _max = nums[i]

        return _max

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # implement count sort and count the frequency
        if len(nums) == 0:
            return []

        max_elem = self._find_max_element(nums)
        count_nums = [0] * (max_elem + 1)

        for i in range(len(nums)):
            count_nums[nums[i]] += 1

        sum_till_now = 0
        for i in range(0, len(count_nums)):
            temp = count_nums[i]
            count_nums[i] = sum_till_now
            sum_till_now += temp

        print(count_nums)

        output = []
        for i in range(len(nums)):
            output.append(count_nums[nums[i]])

        return output


o = Solution().smallerNumbersThanCurrent([6, 5, 4, 8, 8, 6])
print(o)
