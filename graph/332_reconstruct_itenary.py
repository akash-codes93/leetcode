"""
https://leetcode.com/problems/reconstruct-itinerary/

use a stack to recover from the path
beter explanation on ipad
"""

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)
        ans = []

        for st, en in tickets:
            graph[st].append(en)

        for dst in graph.values():
            dst.sort()

        stack = ["JFK"]
        while stack:
            node = stack[-1]
            edges = graph[node]
            if edges:
                edge = edges.pop(0)
                stack.append(edge)
            else:
                ans.append(node)
                stack.pop()

        return ans[::-1]
