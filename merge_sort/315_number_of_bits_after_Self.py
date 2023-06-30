"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
merge_sort maintain inversion
"""


class Node:
    def __init__(self, val, count_smaller, idx):
        self.val = val
        self.count_smaller = count_smaller
        self.idx = idx


class Solution:
    def countSmaller(self, nums):

        for idx, _i in enumerate(nums):
            nums[_i] = Node(_i, 0, idx)

        def merge(a1, a2):
            i = 0
            j = 0
            final = []
            count = 0
            while i < len(a1) and j < len(a2):

                if a1[i].val <= a2[j].val:
                    a1[i].count_smaller += count
                    final.append(a1[i])
                    i += 1
                else:
                    final.append(a2[j])
                    count += 1
                    j += 1

            while i < len(a1):
                a1[i].count_smaller += count
                final.append(a1[i])
                i += 1

            while j < len(a2):
                final.append(a2[j])
                j += 1

            return final

        def mergeSort(l, r):
            if l == r:
                return [nums[l]]

            if l < r:
                mid = (l + r) // 2
                a1 = mergeSort(l, mid)
                a2 = mergeSort(mid + 1, r)

                return merge(a1, a2)

        final = mergeSort(0, len(nums) - 1)
        final = sorted(final, key=lambda x: x.idx)
        return [i.count_smaller for i in final]
