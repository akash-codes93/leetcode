"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
"""
import math


def perculate_up_max(arr, elem):
    arr.append(elem)
    i = len(arr) - 1

    while i > 0:
        parent = math.ceil(i / 2) - 1
        if arr[parent] > arr[i]:
            break
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def perculate_up_min(arr, elem):
    arr.append(elem)
    i = len(arr) - 1

    while i > 0:
        parent = math.ceil(i / 2) - 1
        if arr[parent] < arr[i]:
            break
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = i
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest, heap_size)


def min_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    smallest = i
    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left

    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, smallest, heap_size)


# class Solution:
#     def kthSmallest(self, matrix, k: int) -> int:
#
#         total_size = len(matrix) ** 2
#         rev = False
#
#         if k > (total_size / 2):
#             k = total_size - k + 1
#             rev = True
#             heapify = min_heapify
#             perculate = perculate_up_min
#         else:
#             heapify = max_heapify
#             perculate = perculate_up_max
#
#         heap = []
#
#         print(k)
#
#         if rev:
#             for i in range(len(matrix) - 1, -1, -1):
#                 for j in range(len(matrix[i]) - 1, -1, -1):
#
#                     if len(heap) < k:
#                         perculate(heap, matrix[i][j])
#                     else:
#                         print(heap, k, matrix[i][j])
#                         if matrix[i][j] > heap[0]:
#                             heap[0] = matrix[i][j]
#                             heapify(heap, 0, len(heap))
#                         else:
#                             break
#         else:
#             for i in range(0, len(matrix)):
#                 for j in range(0, len(matrix[i])):
#
#                     if len(heap) < k:
#                         perculate(heap, matrix[i][j])
#                     else:
#                         print(heap, k)
#                         if matrix[i][j] < heap[0]:
#                             heap[0] = matrix[i][j]
#                             heapify(heap, 0, len(heap))
#                         else:
#                             break
#         print(heap)
#         return heap[0]


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]
        while left + 1 < right:
            mid = left + (right - left) // 2
            print("left:", left)
            print("right:", right)
            print("mid:", mid)
            b = self.countElement(matrix, mid, k)
            print("countElement:", b)
            if b:
                right = mid
            else:
                left = mid

        if self.countElement(matrix, left, k):
            return left
        else:
            return right

    def countElement(self, matrix, mid, k):
        i, j = len(matrix) - 1, 0
        count = 0

        while i >= 0 and j < len(matrix):
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1
        print("count: ", count)
        return count >= k

#
# a = Solution().kthSmallest([[1,6,10,13,14,16,21],[3,10,12,18,22,27,29],[3,15,19,20,23,29,34],[8,15,19,25,27,29,39],
#                         [12,17,24,25,28,29,41],[16,22,27,31,31,33,44],[20,26,28,35,39,41,45]], 38)

a = Solution().kthSmallest([[4,5,10], [6,9,13], [8,11,15]], 8)

print(a)

