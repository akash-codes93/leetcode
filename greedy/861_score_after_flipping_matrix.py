"""
https://leetcode.com/problems/score-after-flipping-matrix/description/?envType=daily-question&envId=2024-05-13
"""
from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        def flip_row(row):
            for i in range(0, n):
                grid[row][i] = 1 - grid[row][i]

        def flip_column(col):
            for i in range(0, m):
                grid[i][col] = 1 - grid[i][col]

        def count_ones(col):
            c = 0
            for i in range(0, m):
                if grid[i][col] == 1:
                    c += 1
            return c

        def score():
            s = 0
            for i in range(0, m):
                for k in range(0, n):
                    s += grid[i][k] * (2 ** (n - k - 1))
            return s

        for j in range(0, m):
            if grid[j][0] != 1:
                flip_row(j)

        for j in range(1, n):
            count = count_ones(j)
            if count < (m/2):
                flip_column(j)

        return score()

