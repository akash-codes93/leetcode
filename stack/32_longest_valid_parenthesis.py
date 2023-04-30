"""
https://leetcode.com/problems/longest-valid-parentheses/

use stack node[value + index]

"""


class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx


class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        count = 0

        for i in range(0, len(s)):
            node = Node(s[i], i)
            if len(stack) == 0:
                stack.append(node)
            else:
                if node.val == ')' and stack[-1].val == '(':
                    stack.pop()
                else:
                    stack.append(node)

        if len(stack) == 0:
            return len(s)
        else:
            max_value = len(s)
            count = 0
            while len(stack) != 0:
                node = stack.pop()
                diff = max_value - node.idx - 1
                if diff > count:
                    count = diff

                max_value = node.idx

        # for last case
        if max_value > count:
            return max_value

        return count