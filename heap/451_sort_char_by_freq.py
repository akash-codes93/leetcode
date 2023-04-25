"""
https://leetcode.com/problems/sort-characters-by-frequency/description/

priority queue game

"""
import math


class Node:

    def __init__(self, elem, freq):
        self.freq = freq
        self.elem = elem


def max_heapify(arr, i, heap_size):
    left = 2*i+1
    right = 2*i+2

    largest = i

    if left < heap_size and arr[left].freq > arr[largest].freq:
        largest = left

    if right < heap_size and arr[right].freq > arr[largest].freq:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]

        max_heapify(arr, largest, heap_size)



def build_heap(arr):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        max_heapify(arr, i, len(arr))


class Solution:
    def frequencySort(self, s: str) -> str:

        d = {}

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        arr = []
        for k, v in d.items():
            arr.append(Node(k, v))

        build_heap(arr)

        st = ''
        p = 1
        for i in range(len(arr) - 1, -1, -1):
            node = arr[0]
            st += node.elem * node.freq

            arr[i], arr[0] = arr[0], arr[i]

            max_heapify(arr, 0, len(arr) - p)
            p += 1

        return st


# a = Solution().frequencySort("tree")
# a = Solution().frequencySort("cccaaa")
a = Solution().frequencySort("Aabb")
print(a)
