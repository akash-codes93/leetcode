"""
https://leetcode.com/problems/merge-k-sorted-lists/

build priority queue of k size. min_heap
then extract min element, (replace with next element or last element of heap) heapify again
until all linked list are finished.

Time = NlogK
Space: O(1)

"""
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def min_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    smallest = i

    if left < heap_size and arr[left].val < arr[smallest].val:
        smallest = left

    if right < heap_size and arr[right].val < arr[smallest].val:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, smallest, heap_size)


def build_heap(arr):
    for i in range(math.floor(len(arr) / 2), -1, -1):
        min_heapify(arr, i, len(arr))


class Solution:
    def mergeKLists(self, lists):

        if not lists:
            return []

        arr = []

        for i in range(0, len(lists)):
            if lists[i]:
                arr.append(lists[i])

        build_heap(arr)
        prev = None
        head = None

        while arr:

            node = arr[0]
            if head is None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node

            if prev.next:
                arr[0] = prev.next
            else:
                arr[0] = arr[-1]
                arr.pop()

            min_heapify(arr, 0, len(arr))

        return head
