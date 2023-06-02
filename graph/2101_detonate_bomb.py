"""
https://leetcode.com/problems/detonate-the-maximum-bombs/description/
"""
import math
from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs) -> int:

        def point_exists(x1, y1, x2, y2, r):
            return r >= math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i == j: continue

                if point_exists(bombs[i][0], bombs[i][1], bombs[j][0], bombs[j][1], bombs[i][2]):
                    graph[i].append(j)

        def dfs(visited, node):
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    dfs(visited, n)

        max_visited = 0
        for i in range(len(bombs)):
            visited = set()
            visited.add(i)
            dfs(visited, i)
            max_visited = max(max_visited, len(visited))

        return max_visited

