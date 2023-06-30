"""

"""
import bisect
import random


class Node:

    def __init__(self, prob, index):
        self.prob = prob
        self.index = index


class SolutionUsingProb:

    def __init__(self, w):
        self.w = w
        self.total = sum(w)
        self.prob_arr = self.prepare_probability()

    def prepare_probability(self):
        arr = []
        for idx, _w in enumerate(self.w):
            arr.append(Node(_w/self.total, idx))
        return arr

    def pickIndex(self) -> int:
        p = random.randint(0, len(self.prob_arr)-1)
        val = self.prob_arr[p]
        val.prob -= 1/self.total
        if val.prob <= 0:
            self.prob_arr[p] = self.prob_arr[-1]
            self.prob_arr.pop()

        if not self.prob_arr:
            self.prob_arr = self.prepare_probability()

        return val.index

"""
Find moving sum
[1,2,3] -> [1,3,6]
generate random number and check which bucket it lies and return idx
"""


class Solution:

    def __init__(self, w):
        self.w = w
        self.total = 0
        self.arr = []
        for i in w:
            self.total += i
            self.arr.append(self.total)

    def pickIndex(self) -> int:
        p = random.randint(0, self.total)
        return bisect.bisect_left(self.arr, p)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
