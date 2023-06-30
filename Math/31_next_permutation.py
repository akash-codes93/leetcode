"""
https://leetcode.com/problems/next-permutation/
this has a important concept

Example: 4325413 -> we can only change the last two numbers and have 432531
What if it was 432531 in the first place? 31 cannot be increased.
Let's try 531 - still no
2531 - this can be increased - the smallest number that can be used to increase the 2 is 3. so for now we have 3521.
Next we want to minimize 3521 - that's easier - just sort the numbers to the right of 3 - 3125. So the answer is 4323125
"""


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1

        if i == -1:
            nums.reverse()
            return

        j = len(nums) - 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[:i:-1]
        return
