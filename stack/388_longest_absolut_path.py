"""
https://leetcode.com/problems/longest-absolute-file-path/description/
"""


class Node:

    def __init__(self, total_len, tab_size):
        self.total_len = total_len
        self.tab_size = tab_size


class Solution:
    def lengthLongestPath(self, input: str) -> int:

        # stack

        file_dir = input.split('\n')
        stack = []
        max_size = 0

        for f in file_dir:
            f = f.split('\t')

            tabs = len(f) - 1

            file_or_dir = f[-1]
            is_file = '.' in file_or_dir

            while stack and stack[-1].tab_size >= tabs:
                stack.pop()

            total_len = stack[-1].total_len + len(file_or_dir) + 1 if stack else len(file_or_dir)

            stack.append(Node(total_len, tabs))
            if is_file:
                max_size = max(total_len, max_size)

        return max_size
