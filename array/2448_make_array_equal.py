"""
Weighted median question
"""


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        arr = [[nums[i], cost[i]] for i in range(len(nums))]
        arr = sorted(arr, key=lambda x: x[0])

        def get_costs(median):
            return sum([abs(median - num) * c for num, c in arr])

        total_sum = 0
        for _, cost in arr:
            total_sum += cost

        # print(total_sum)
        median = (total_sum + 1) // 2
        # print(median)
        median_elem = arr[0][1]

        for num, cost in arr:
            median -= cost
            if median <= 0:
                median_elem = num
                break
        # print(median_elem)
        return get_costs(median_elem)
