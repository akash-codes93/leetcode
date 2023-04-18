"""
https://leetcode.com/problems/combinations/
"""

import copy


class Solution:
    def combine(self, n: int, k: int):
        main_output = []

        def looper(i, path):
            if len(path) == k:
                main_output.append(copy.copy(path))
                return

            if i > n:
                return

            for j in range(i, n + 1):
                path.append(j)
                looper(j + 1, path)
                path.pop()

        looper(1, [])

        return main_output