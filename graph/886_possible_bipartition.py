"""
https://leetcode.com/problems/possible-bipartition/
"""

from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = [-1] * (n + 1)

        def isGraphBipartite(i):

            queue = [i]
            color[i] = 1

            while queue:
                v = queue.pop(0)
                valid_color = 1 - color[v]
                for v1 in graph[v]:
                    if color[v1] == -1:
                        color[v1] = valid_color
                        queue.append(v1)

                    elif color[v1] != valid_color:
                        return False

            return True

        for i in range(1, n + 1):
            if color[i] == -1:
                if not isGraphBipartite(i):
                    return False

        return True