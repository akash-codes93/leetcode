"""
287: O(n) but array is changed
"""


class SolutionSwapSort:

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


# you can also use O(n) space to create set and check for duplicate elements


# you cannot also use moore's voting algorithm as freq should be more than n/2


# you can also use binary search since elements are bw [1, n]
"""
According to the Pigeon hole Principle, n+1 integers, placed in an array of length n, at least 1 integer will be repeated.

So guess a number first(the number mid in the valid range [left,right]), count the elements of the array which is less 
than or equal to mid in the array.

If cnt is strictly greater than mid. According to the Pigeonhole Principle, repeated elements are in the 
interval [left,mid];
Otherwise, the repeated element is in the interval [mid+1, right].

"""


class Solution:

    def findDuplicate(self, nums):
        # binary search
        lt = 1
        rt = len(nums) - 1
        while lt <= rt:
            mid = (lt + rt) // 2

            # apply Pigeon hole principle
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count <= mid:
                lt = mid + 1
            else:
                rt = mid - 1

        return lt

# tortoise hare method detection
