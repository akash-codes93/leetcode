import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        m = len(heights)
        n = len(heights[0])

        def get_neighbours(i, j):
            out = []
            adds = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for x, y in adds:
                if 0 <= (i + x) < m and 0 <= (j + y) < n:
                    out.append((i + x, j + y))
            return out

        minHeap = [(0, 0, 0)]
        visited = set()

        while minHeap:

            diff, x, y = heapq.heappop(minHeap)

            if (x, y) == (m-1, n-1):
                return diff

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for x1, y1 in get_neighbours(x, y):
                newDiff = max(diff, abs(heights[x1][y1] - heights[x][y]))

                if (x1, y1) not in visited:
                    heapq.heappush(minHeap, (newDiff, x1, y1,))

        return -1