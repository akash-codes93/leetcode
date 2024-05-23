"""
https://leetcode.com/problems/path-with-maximum-gold/?envType=daily-question&envId=2024-05-14
backtracking
"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def neighbour(x, y):
            out = []
            adds = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for p, q in adds:
                if 0 <= (p + x) < m and 0 <= (q + y) < n:
                    out.append((p + x, q + y))
            return out

        def dfs(x, y, visited, gold):

            max_gold = 0
            for x1, y1 in neighbour(x, y):
                if (x1, y1) not in visited and grid[x1][y1] != 0:
                    visited.add((x1, y1))
                    max_gold = max(max_gold, dfs(x1, y1, visited, grid[x1][y1]))
                    visited.remove((x1, y1))

            return gold + max_gold

        max_g = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] != 0:
                    max_g = max(max_g, dfs(i, j, {(i, j)}, grid[i][j]))
        return max_g
