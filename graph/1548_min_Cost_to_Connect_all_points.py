"""
Djikstra
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = defaultdict(list)

        for i in range(0, len(points)):

            x1, y1 = points[i]
            for j in range(0, len(points)):

                if i == j:
                    continue

                x2, y2 = points[j]
                graph[(x1, y1)].append((x2, y2))

        heap = [(0, points[0][0], points[0][1])]
        visited = set()
        cost = 0

        while heap:
            _cost, x1, y1 = heapq.heappop(heap)
            if (x1, y1) in visited:
                continue

            visited.add((x1, y1))
            cost += _cost

            for x2, y2 in graph[(x1, y1)]:
                if (x2, y2) not in visited:
                    c = abs(x2 - x1) + abs(y2 - y1)
                    heapq.heappush(heap, (c, x2, y2))

        return cost

