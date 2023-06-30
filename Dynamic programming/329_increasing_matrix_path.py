"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

same approach as 2328
"""

class Solution:
    def longestIncreasingPath(self, matrix) -> int:

        m = len(matrix)
        n = len(matrix[0])

        def find_neighbour(i, j):
            o = []

            if i + 1 < m:
                o.append((i + 1, j))

            if i - 1 >= 0:
                o.append((i - 1, j))

            if j + 1 < n:
                o.append((i, j + 1))

            if j - 1 >= 0:
                o.append((i, j - 1))

            return o

        dp = [[1] * n for _ in range(m)]

        cells = sorted(
            [
                [i, j] for j in range(n)
                for i in range(m)
            ],
            key=lambda x: matrix[x[0]][x[1]]
        )
        max_len = 1
        for cell in cells:
            for neigh in find_neighbour(cell[0], cell[1]):
                if matrix[cell[0]][cell[1]] < matrix[neigh[0]][neigh[1]]:
                    dp[neigh[0]][neigh[1]] = max(dp[neigh[0]][neigh[1]], 1 + dp[cell[0]][cell[1]])
                    max_len = max(max_len, dp[neigh[0]][neigh[1]])

        return max_len


