"""
https://leetcode.com/problems/construct-the-rectangle/

The W is always less than or equal to the square root of the area,
so we start searching at sqrt(area) till we find the result.

"""
import math
from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        w = math.floor(math.sqrt(area))
        ans = [0, 0]
        difference = area

        while w >= 1:

            if area % w == 0:

                l = area // w

                if (l - w) < difference:
                    ans = [l, w]
                    difference = l - w

            w = w - 1

        return ans


print(

    Solution().constructRectangle(37),
    Solution().constructRectangle(56),
    Solution().constructRectangle(12212),



)


