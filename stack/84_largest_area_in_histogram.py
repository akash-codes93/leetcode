"""
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

for a height[i] => area[i] = (nsr[i] - nsl[i] -1) * height[i]

draw the diagram and check nsr and nsl

please implement nsr, nsl, ngr, ngl [very useful in stack]

"""


class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index


class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:

        stack = []
        nsr = []

        for i in range(len(arr) - 1, -1, -1):
            if len(stack) == 0:
                nsr.append(len(arr))
            else:

                while len(stack) > 0 and arr[i] <= stack[-1].val:
                    stack.pop()

                if len(stack) == 0:
                    nsr.append(len(arr))
                else:
                    nsr.append(stack[-1].index)
            stack.append(Node(arr[i], i))

        nsr.reverse()
        stack = []
        nsl = []

        for i in range(0, len(arr)):
            if len(stack) == 0:
                nsl.append(-1)
            else:

                while len(stack) > 0 and arr[i] <= stack[-1].val:
                    stack.pop()

                if len(stack) == 0:
                    nsl.append(-1)
                else:
                    nsl.append(stack[-1].index)
            stack.append(Node(arr[i], i))

        print(nsr)
        print(nsl)
        area = [(nsr[i] - nsl[i] - 1) * arr[i] for i in range(0, len(arr))]

        return max(area)
