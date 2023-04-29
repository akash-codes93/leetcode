"""
https://leetcode.com/problems/maximal-rectangle/

explanation on ipad
create buildings after that find mah on them

"""


class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index


def largestRectangleArea(arr) -> int:

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



class Solution:
    def maximalRectangle(self, matrix) -> int:

        max_mah = 0
        heights = [0] * len(matrix[0])

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):

                if matrix[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += int(matrix[i][j])

            mah = largestRectangleArea(heights)
            if mah > max_mah:
                max_mah = mah

        return max_mah

a = Solution().maximalRectangle( matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(a)