"""
268
"""


class Solution:
    def missingNumber(self, nums) -> int:

        # cyclic sort or swap sort
        nums.append(0)

        # processing part
        i = 0
        while i < len(nums):

            if nums[i] != nums[nums[i]]:
                p = nums[i]
                nums[i] = nums[nums[i]]
                nums[p] = p
            else:
                i += 1
        # observation part
        for i in range(0, len(nums)):
            if nums[i] != i:
                return i

        # if all number matches then 0 is the custom added number
        return 0


a = Solution().missingNumber([3, 0, 1])
# print(a)

"""
442
"""


class Solution:
    def findDuplicates(self, nums):

        out = []

        # processing part
        i = 0
        while i < len(nums):

            if nums[i] != nums[nums[i] - 1]:
                p = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = p
            else:
                i += 1

        # observation part
        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                out.append(nums[i])

        return out

Solution()

"""
287
"""
class Solution:
    def findDuplicate(self, nums) -> int:

        # processing part
        i = 0
        while i < len(nums):

            if nums[i] != nums[nums[i] - 1]:
                p = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = p
            else:
                i += 1

        # observation part
        for i in range(0, len(nums)):
            if nums[i] != i + 1:
                return nums[i]
