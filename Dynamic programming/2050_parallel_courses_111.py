"""
https://leetcode.com/problems/parallel-courses-iii/description/
"""

from collections import defaultdict


class Node:

    def __init__(self, val, time, st=0, en=0):
        self.st = st
        self.en = en
        self.val = val
        self.time = time


class Solution:
    def minimumTime(self, n: int, relations, times) -> int:

        eout = defaultdict(set)
        ein = defaultdict(set)
        node_map = {}

        def link(_from, to):
            eout[_from].add(to)
            ein[to].add(_from)

        def unlink(_from, to):
            eout[_from].remove(to)
            ein[to].remove(_from)

        zero_in_deg = lambda x: len(ein[x]) == 0

        for i in range(1, n+1):
            node_map[i] = Node(i, times[i-1])

        for _from, to in relations:
            link(_from, to)

        queue = []
        for i in range(1, n + 1):
            if zero_in_deg(i):
                node = node_map[i]
                node.st = 0
                queue.append(node)

        time = 0
        while queue:

            node = queue.pop(0)
            print(node.val, node.st)
            node.en = node.st + node.time
            time = max(time, node.en)

            for each_node_val in tuple(eout[node.val]):
                unlink(node.val, each_node_val)
                each_node = node_map[each_node_val]
                each_node.st = max(each_node.st, node.en)
                if zero_in_deg(each_node_val):
                    queue.append(each_node)

        print(time)
        return time


Solution().minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5])
