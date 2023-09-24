"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""
import math
from typing import List


class Node:
    def __init__(self, row, soldiers):
        self.row = row
        self.soldier = soldiers

    def __lt__(self, other):
        if self.soldier < other.soldier:
            return True
        elif self.soldier == other.soldier and self.row < other.row:
            return True

        return False


def min_heapify(arr, i, size):
    left = 2 * i + 1
    right = 2 * i + 2

    smallest = i

    if left < size and arr[left] < arr[smallest]:
        smallest = left

    if right < size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest, size)


def perculate_up(arr, node):
    arr.append(node)
    i = len(arr) - 1
    while i > 0:
        parent = math.ceil(i / 2) - 1

        if arr[parent] < arr[i]:
            break
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def build_heap(arr):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        min_heapify(arr, i, len(arr))


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        arr = []
        for idx, nums in enumerate(mat):
            arr.append(Node(idx, sum(nums)))

        build_heap(arr)
        output = []
        while k > 0:
            node = arr[0]
            arr[0] = arr[-1]
            arr.pop()
            min_heapify(arr, 0, len(arr))

            output.append(node.row)
            k -= 1

        return output


solution = Solution()
# ans = solution.kWeakestRows(mat =
# [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]],
# k = 3)

# ans = solution.kWeakestRows(mat =
# [[1,0,0,0],
#  [1,1,1,1],
#  [1,0,0,0],
#  [1,0,0,0]],
# k = 2)

ans = solution.kWeakestRows(mat=
                            [[1, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0],
                             [1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 1, 0]],
                            k=5)

print(ans)
