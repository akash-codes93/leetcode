"""
https://leetcode.com/problems/ipo/
two heaps:
max heap [on profit] with capital < w
min heap [on capital] with capital > w
"""

import math


class Node:
    def __init__(self, profit, capital):
        self.capital = capital
        self.profit = profit


def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < heap_size and arr[left].profit > arr[largest].profit:
        largest = left

    if right < heap_size and arr[right].profit > arr[largest].profit:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest, heap_size)


def min_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    if left < heap_size and arr[left].capital < arr[smallest].capital:
        smallest = left

    if right < heap_size and arr[right].capital < arr[smallest].capital:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, smallest, heap_size)


def max_perculate_up(arr, node):
    arr.append(node)
    i = len(arr) - 1

    while i > 0:
        parent = math.ceil(i / 2) - 1
        if arr[parent].profit > arr[i].profit:
            break

        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def min_perculate_up(arr, node):
    arr.append(node)
    i = len(arr) - 1

    while i > 0:
        parent = math.ceil(i / 2) - 1
        if arr[parent].capital < arr[i].capital:
            break

        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:

        tasks = []
        for i in range(len(profits)):
            tasks.append(Node(profits[i], capital[i]))

        max_heap = []
        min_heap = []
        for task in tasks:
            if task.capital <= w:
                max_perculate_up(max_heap, task)
            else:
                min_perculate_up(min_heap, task)

        while True:
            # print([[task.profit, task.capital] for task in max_heap])
            # print([[task.profit, task.capital] for task in min_heap])
            if k == 0 or len(max_heap) == 0:
                break

            task = max_heap[0]
            w = (w + max_heap[0].profit)
            # print(w)
            max_heap[0] = max_heap[-1]
            max_heap.pop()
            max_heapify(max_heap, 0, len(max_heap))

            while min_heap and min_heap[0].capital <= w:
                max_perculate_up(max_heap, min_heap[0])
                min_heap[0] = min_heap[-1]
                min_heap.pop()
                min_heapify(min_heap, 0, len(min_heap))

            k -= 1

        return w
