"""
https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
"""


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        A = [i + 1 for i in range(n)]
        i = 0
        while len(A) != 1:
            i = (i + k - 1) % len(A)
            del A[i]
        return A[0]
