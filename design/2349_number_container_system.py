"""
https://leetcode.com/problems/design-a-number-container-system/
same as 2345

two maps
{
element: heap(indexes)
}

{
index: element
}

"""
import math
from collections import defaultdict


def heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    smallest = i
    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left

    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, smallest, heap_size)


def perculate_up(arr, elem):
    arr.append(elem)
    i = len(arr) - 1

    while i > 0:
        parent = math.ceil(i / 2) - 1
        if arr[parent] < arr[i]:
            break
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


class NumberContainers:

    def __init__(self):
        self.heap_map = defaultdict(list)
        self.index_map = {}

    def change(self, index: int, number: int) -> None:

        self.index_map[index] = number
        heap = self.heap_map[number]

        perculate_up(heap, number)

    def find(self, number: int) -> int:
        heap = self.heap_map[number]

        while len(heap):
            index = heap[0]
            if number != self.index_map[index]:
                heap[0] = heap[-1]
                heap.pop()
                heapify(heap, 0, len(heap))
            else:
                return index

        return -1
