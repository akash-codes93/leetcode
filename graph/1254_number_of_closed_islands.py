"""
https://leetcode.com/problems/number-of-closed-islands/

same as flood fill with one extra case

"""

from collections import deque


class Solution:

    def closedIsland(self, grid) -> int:

        n = len(grid)
        m = len(grid[0])

        def find_neighbour(i, j):
            out = []
            if i - 1 >= 0:
                out.append((i - 1, j))

            if i + 1 < m:
                out.append((i + 1, j))

            if j - 1 >= 0:
                out.append((i, j - 1))

            if j + 1 < n:
                out.append((i, j + 1))

            return out

        def apply_bfs(i, j):
            queue = deque([(i, j)])
            visited = {(i, j)}
            while queue:
                x, y = queue.popleft()
                grid[x][y] = 1
                for x1, y1 in find_neighbour(x, y):
                    if grid[x1][y1] == 0:
                        visited.add((x1, y1))
                        queue.append((x1, y1))

        for p in range(0, m):
            if grid[0][p] == 0:
                apply_bfs(0, p)

            if grid[n - 1][p] == 0:
                apply_bfs(n - 1, p)

        for p in range(0, n):
            if grid[p][0] == 0:
                apply_bfs(p, 0)

            if grid[p][m - 1] == 0:
                apply_bfs(p, m - 1)

        no_of_islands = 0

        for p in range(0, n):
            for q in range(0, m):

                if grid[p][q] == 0:
                    no_of_islands += 1
                    apply_bfs(p, q)

        return no_of_islands
