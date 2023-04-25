"""
https://leetcode.com/problems/online-stock-span/

use stack to main smaller element

similar to next smaller element to left
"""


class Node:

    def __init__(self, val, popped):
        self.val = val
        self.popped = popped


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        n = Node(price, 0)
        while len(self.stack) > 0 and self.stack[-1].val <= n.val:
            a = self.stack.pop()
            n.popped += a.popped + 1
        self.stack.append(n)

        return n.popped + 1