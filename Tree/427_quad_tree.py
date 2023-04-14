"""
@Quad tree
@url: https://leetcode.com/problems/construct-quad-tree/

Idea: top left cell is the key
so the value at top left cell is equal to all the values that means it is a leaf node


Time: n2 * log n

"""

from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:

    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n, r, c):
            all_same = True

            for i in range(0, n):
                for j in range(0, n):

                    if grid[r][c] != grid[r+i][c+j]:
                        all_same = False

            if all_same:
                return Node(0, True, None, None, None, None)

            n = n//2

            top_left = dfs(n, r, c)
            top_right = dfs(n, r, c+n)
            bottom_left = dfs(n, r+n, c)
            bottom_right = dfs(n, r+n, c+n)

            return Node(1, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(len(grid), 0, 0)

