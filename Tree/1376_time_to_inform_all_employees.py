"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/
"""

from collections import defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager, informTime) -> int:

        graph = defaultdict(list)

        for i in range(n):
            graph[manager[i]].append(i)

        def dfs(node, time):

            new_time = time + informTime[node]
            max_time = new_time
            for sub in graph[node]:
                max_time = max(max_time, dfs(sub, new_time))

            return max_time

        return dfs(headID, 0)
