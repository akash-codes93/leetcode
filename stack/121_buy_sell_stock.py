"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

same as water trapping problem
maintain greater element to right [extra space]
take diff

we can do this with one varibale below is example of that

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # same as water trapping problem

        # maintain greatest to the right in an array
        # take diff with array and max profit

        max_right = 0
        max_profit = 0

        for i in range(len(prices) - 1, -1, -1):

            if prices[i] > max_right:
                max_right = prices[i]

            diff = max_right - prices[i]

            if max_profit < diff:
                max_profit = diff

        return max_profit