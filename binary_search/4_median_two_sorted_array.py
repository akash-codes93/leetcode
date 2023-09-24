"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description
"""


class Solution:

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        l = 0
        r = len(nums1) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2  # do the calculation

            first_left = float('-inf') if i < 0 else nums1[i]
            first_right = nums1[i + 1] if i + 1 < len(nums1) else float('inf')

            second_left = float('-inf') if j < 0 else nums2[j]
            second_right = nums2[j + 1] if j + 1 < len(nums2) else float('inf')

            if first_left <= second_right and second_left <= first_right:
                if total % 2:
                    # odd case
                    return min(first_right, second_right)
                # even case
                return (max(first_left, second_left) + min(first_right, second_right)) / 2
            elif first_left > second_right:
                r = i - 1
            else:
                l = i + 1

