"""
https://leetcode.com/problems/all-paths-from-source-to-target/description/
"""

import copy


class Solution:
    def allPathsSourceTarget(self, graph):

        main_path = []

        def helper(i, path):
            if i == len(graph) - 1:
                main_path.append(copy.copy(path))
                return

            for _dir in graph[i]:
                if _dir not in path:
                    path.append(_dir)
                    helper(_dir, path)
                    path.pop()

        helper(0, [0])
        return main_path

p = Solution().allPathsSourceTarget(graph = [[4,3,1],[3,2,4],[3],[4],[]])
print(p)