"""
https://leetcode.com/problems/jewels-and-stones/
"""


class Solution:

    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        jewels_dict = {}
        count = 0

        for i in jewels:
            jewels_dict[i] = 1

        for stone in stones:
            value = jewels_dict.get(stone)
            if value:
                count += 1

        return count


c = Solution().numJewelsInStones(jewels="z", stones="ZZ")
print(c)
