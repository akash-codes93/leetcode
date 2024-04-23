"""

https://leetcode.com/problems/flower-planting-with-no-adjacent/description/

"""

from typing import List
from collections import defaultdict


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        graph = defaultdict(set)

        for x, y in paths:
            graph[x].add(y)  # undirected
            graph[y].add(x)

        colors = [0] * (n + 1)

        def check_if_valid(garden, color):
            for adjacent_garden in graph[garden]:
                if colors[adjacent_garden] == color:
                    return False
            return True

        def dfs(garden):
            if garden > n:
                return True

            for color in range(1, 5):
                if check_if_valid(garden, color):
                    colors[garden] = color
                    return dfs(garden + 1)

            return False

        dfs(1)
        return colors[1:]


# print(Solution().gardenNoAdj(3, paths=[[1, 2], [2, 3], [3, 1]]))
# print(Solution().gardenNoAdj(4, paths=[[1,2],[3,4]]))
print(Solution().gardenNoAdj(4, paths=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))
