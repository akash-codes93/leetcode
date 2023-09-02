"""

Queue approach
"""
from collections import defaultdict


class SolutionQueue:
    def networkDelayTime(self, times, n: int, k: int) -> int:

        # normal

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = [float('inf')] * (n + 1)
        queue = [(k, 0)]
        dist[k] = 0
        dist[0] = 0

        while queue:
            node, time = queue.pop(0)
            for neigh, weight in graph[node]:
                if weight + time < dist[neigh]:
                    dist[neigh] = weight + time
                    queue.append((neigh, weight + time))

        max_time = max(dist)
        if max_time == float('inf'):
            return -1
        return max_time


import math


class Node:
    def __init__(self, node, time):
        self.node = node
        self.time = time


def min_heapify(heap, i, heap_size):
    left = 2*i + 1
    right = 2*i + 2

    smallest = i

    if left < heap_size and heap[left].time < heap[smallest].time:
        smallest = left

    if right < heap_size and heap[right].time < heap[smallest].time:
        smallest = right

    if smallest != i:
        heap[smallest], heap[i] = heap[i], heap[smallest]
        min_heapify(heap, smallest, heap_size)


def perculate_up(heap, node):
    heap.append(node)
    i = len(heap) - 1

    while i > 0:
        parent = math.ceil(i/2) - 1

        if heap[parent].time < heap[i].time:
            break

        heap[parent], heap[i] = heap[i], heap[parent]
        i = parent


class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:

        # normal

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        heap = [Node(k, 0)]

        visited = set()
        t = 0

        while heap:

            node = heap[0]

            heap[0] = heap[-1]
            heap.pop()
            min_heapify(heap, 0, len(heap))

            if node.node in visited:
                continue

            visited.add(node.node)
            t = max(node.time, t)

            for neigh, time in graph[node.node]:
                if neigh not in visited:
                    perculate_up(heap, Node(neigh, node.time + time))

        return t if len(visited) == n else -1



