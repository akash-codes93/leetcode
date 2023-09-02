"""
https://leetcode.com/problems/dungeon-game/
we need to travel bottom right
and dp[i][j] > 0 then dp[i][j] = 0
"""


class Node:

    def __init__(self, _sum, min_val):
        self.sum = _sum
        self.min_val = min_val


class Solution:
    def calculateMinimumHP(self, dungeon) -> int:

        dp = [[0] * len(dungeon[0]) for _ in range(0, len(dungeon))]

        for i in range(0, len(dp)):
            for j in range(0, len(dp[i])):

                if i == 0 and j == 0:
                    dp[i][j] = Node(dungeon[i][j], dungeon[i][j])

                elif i == 0:
                    dp[i][j] = Node(dp[i][j - 1].sum + dungeon[i][j],
                                    min(dp[i][j - 1].min, dungeon[i][j])
                                    )

                elif j == 0:
                    dp[i][j] = Node(dp[i - 1][j].sum + dungeon[i][j],
                                    min(dp[i - 1][j].min, dungeon[i][j])
                                    )
                else:

                    n1 = Node(dp[i][j - 1].sum + dungeon[i][j],
                              min(dp[i][j - 1].min, dungeon[i][j])
                              )
                    n2 = Node(dp[i - 1][j].sum + dungeon[i][j],
                              min(dp[i - 1][j].min, dungeon[i][j])
                              )

                    n1val = min(n1.sum, n1.val)
                    n2val = min(n2.sum, n2.val)

                    if n1val < 0 and n2val < 0:
                        if n1val < n2val:
                            dp[i][j] = n2
                        else:
                            dp[i][j] = n1
                    else:
                        if n1val < n2val:
                            dp[i][j] = n1
                        else:
                            dp[i][j] = n2

        print(dp)
        return dp[-1][-1]
