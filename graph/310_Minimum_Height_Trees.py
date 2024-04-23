"""
https://leetcode.com/problems/minimum-height-trees/description/?envType=daily-question&envId=2024-04-23

can be soved using kahn's algorithm
or diameter of tree


"""

from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        is_node_leaf = lambda x: len(graph[x]) in [1, 0]  # 0 for unconnected components

        queue = []
        other_queue = []
        for i in range(n):
            if is_node_leaf(i):
                queue.append(i)

        while queue and len(graph) > 2:
            # print(graph, queue)
            nd = queue.pop(0)

            for nei in tuple(graph[nd]):
                graph[nei].remove(nd)

                if is_node_leaf(nei):
                    other_queue.append(nei)

            graph.pop(nd)
            if len(queue) == 0:
                # print("queue zero", graph, queue, other_queue)
                if len(graph) <= 2:
                    break
                queue = other_queue
                other_queue = []

        # print(other_queue, queue)
        if not other_queue:  # case when there is no edge n=1 edge=[]
            return queue
        return other_queue


# print(Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
# print(Solution().findMinHeightTrees(1, []))
print(Solution().findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]]))
