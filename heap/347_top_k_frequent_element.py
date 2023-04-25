"""
https://leetcode.com/problems/top-k-frequent-elements/
"""
import math


class Node:

    def __init__(self, element, frequency):
        self.element = element
        self.frequency = frequency


def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = i

    if (left < heap_size and arr[left].frequency > arr[largest].frequency):
        largest = left

    if (right < heap_size and arr[right].frequency > arr[largest].frequency):
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest, heap_size)


def build_heap(arr):
    for i in range(math.floor(len(arr)) - 1, -1, -1):
        max_heapify(arr, i, len(arr))


class Solution:

    def topKFrequent(self, nums, k: int):
        hash_map = {}

        for elem in nums:
            if elem in hash_map:
                hash_map[elem] += 1
            else:
                hash_map[elem] = 1

        arr = []
        for key, value in hash_map.items():
            arr.append(Node(key, value))

        print(hash_map)

        build_heap(arr)

        ans = []
        # print([i.element for i in arr])
        # print([i.frequency for i in arr])
        p = 1
        for i in range(len(arr) - 1, (len(arr) - k) - 1, -1):
            ans.append(arr[0].element)
            arr[0], arr[i] = arr[i], arr[0]
            max_heapify(arr, 0, len(arr) - p)
            p += 1

        return ans


# a = Solution().topKFrequent([1,2,2,1,3,3,3,4,4,4,], 3)
# a = Solution().topKFrequent([1], 1)
a = Solution().topKFrequent([5, 3, 1, 1, 1, 3, 5, 73, 1], 3)
print(a)
