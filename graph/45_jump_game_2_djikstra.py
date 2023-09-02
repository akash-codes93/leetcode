"""

"""


class Solution:
    def jump(self, nums: List[int]) -> int:

        # dp = [float('inf')] * len(nums)
        # dp[0] = 0

        # for i in range(1, len( nums)):
        #     for j in range(0, i):

        #         if nums[j] + j >= i and dp[j] + 1 < dp[i]:
        #             dp[i] = dp[j] +1

        # # print(dp)
        # return dp[-1]

        # bfs
        # queue = [(0, 0)]
        # visited = {0}
        # min_time = float('inf')

        # while queue:
        #     n = queue.pop(0)
        #     if n[0] == len(nums)-1 and n[1] < min_time:
        #         min_time = n[1]

        #     for i in range(1, nums[n[0]]+1):
        #         new_pos = n[0] + i
        #         if new_pos < len(nums) and new_pos not in visited:
        #             visited.add(new_pos)
        #             queue.append((new_pos, n[1]+1))

        # return min_time

        # optimised greedy

        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1

        return res

        # djisktra
        # (jump, pos)
        n = len(nums)
        arr = [(0, 0)]
        visited = set()

        while arr:
            jump, pos = heapq.heappop(arr)
            # print(jump, pos)
            if pos == n - 1:
                return jump

            if pos in visited:
                continue
            visited.add(pos)

            for val in range(1, nums[pos] + 1):

                if (pos + val) not in visited:
                    heapq.heappush(arr, (jump + 1, pos + val))

