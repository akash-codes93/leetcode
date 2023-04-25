"""
https://leetcode.com/problems/sliding-window-maximum/description/

make a heap with Node(elem, index) of K
if top element is outside window
pop it out and re heapify

time nlogk

better solution with dequeue O(N)

"""
import math


class Node:

    def __init__(self, val, idx):
        self.val = val
        self.idx = idx


def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = i

    if left < heap_size and arr[left].val > arr[largest].val:
        largest = left

    if right < heap_size and arr[right].val > arr[largest].val:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest, heap_size)


def perculate_up(arr, num):
    arr.append(num)
    i = len(arr) - 1

    while i > 0:

        parent = math.ceil(i / 2) - 1
        if (arr[parent].val > arr[i].val):
            break

        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


class Solution:
    def maxSlidingWindow(self, nums, k: int):

        ans = []
        arr = []
        for i in range(0, len(nums)):
            perculate_up(arr, Node(nums[i], i))

            if i >= (k-1):
                while arr[0].idx < (i - k + 1):
                    arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]
                    arr.pop()
                    max_heapify(arr, 0, len(arr))
                ans.append(arr[0].val)
        return ans


# a = Solution().maxSlidingWindow([1,3,-1,-3,5], 3)
a = Solution().maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5)
print(a)