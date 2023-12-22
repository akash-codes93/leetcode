import heapq


class Solution:
    def candy(self, ratings) -> int:

        heap = [(ratings[i], i) for i in range(0, len(ratings))]

        heapq.heapify(heap)
        n = len(ratings)
        candies = [1] * n

        while heap:

            _, idx = heapq.heappop(heap)

            if idx > 0 and ratings[idx - 1] > ratings[idx] and candies[idx - 1] <= candies[idx]:
                candies[idx - 1] = candies[idx] + 1

            if idx < n - 1 and ratings[idx + 1] > ratings[idx] and candies[idx + 1] <= candies[idx]:
                candies[idx + 1] = candies[idx] + 1

        print(candies)
        return sum(candies)


s = Solution().candy([10, 40, 200, 1000, 60, 30])
print(s)
