"""
https://leetcode.com/problems/k-closest-points-to-origin/?envType=list&envId=oc2pg8hr

build max heap and check with 0th index element if greater than leave else replace and pop

"""
import math


class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.d = x * x + y * y


def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = i
    if left < heap_size and arr[left].d > arr[largest].d:
        largest = left

    if right < heap_size and arr[right].d > arr[largest].d:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest, heap_size)


def perculate_up(arr, node):
    arr.append(node)
    i = len(arr) - 1

    while i > 0:
        parent = math.ceil(i / 2) - 1

        if arr[parent].d > arr[i].d:
            break

        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


# class Solution:
#     def kClosest(self, points, k):
#         arr = []
#         for point in points:
#
#             if len(arr) < k:
#                 perculate_up(arr, Node(point[0], point[1]))
#             else:
#                 node = Node(point[0], point[1])
#                 if arr[0].d > node.d:
#                     arr[0] = node
#                     max_heapify(arr, 0, len(arr))
#
#         return [[p.x, p.y] for p in arr]


"""
Quick select average time complexity O(N)
"""


def get_partition(arr, l, r):
    pivot = arr[r].d
    i = l

    for j in range(l, r):
        if arr[j].d < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[r] = arr[r], arr[i]
    return i


class Solution:

    def kClosest(self, points, k):

        arr = []

        for point in points:
            arr.append(
                Node(point[0], point[1])
            )

        def quick_select(l, r, k):
            if l >= r:
                return
            idx = get_partition(arr, l, r)
            print(l, r, idx, k)
            if (k + l) < idx + 1:
                quick_select(l, idx - 1, k)
            elif (k + l) > idx + 1:
                quick_select(idx + 1, r, (k + l) - (idx + 1))  # idx + 1 is the new l  || k is actually the distance from l -> so actual position of k is (k+l)

        quick_select(0, len(arr) - 1, k)
        return [[arr[i].x, arr[i].y] for i in range(0, k)]


p = Solution().kClosest([[6, 10], [-3, 3], [-2, 5], [0, 2]], 3)
print(p)
