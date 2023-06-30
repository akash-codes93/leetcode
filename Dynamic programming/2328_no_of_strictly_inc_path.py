"""
recursive dfs
"""


class Solution:
    def countPaths(self, grid) -> int:

        m = len(grid)
        n = len(grid[0])

        # dp = [[1] * n for _ in range(m)]

        def find_neighbour(i, j):
            o = []

            if i + 1 < m:
                o.append((i + 1, j))

            if i - 1 >= 0:
                o.append((i - 1, j))

            if j + 1 < n:
                o.append((i, j + 1))

            if j - 1 >= 0:
                o.append((i, j - 1))

            return o

        cnt = 0
        mem = {}

        def dfs(i, j, visited):
            # print("st:", i,j, visited)

            if (i, j) in mem:
                return mem[(i, j)]

            neighs = find_neighbour(i, j)
            count = 0
            for neigh in neighs:
                if neigh not in visited:
                    visited.add(neigh)
                    if grid[i][j] < grid[neigh[0]][neigh[1]]:
                        # print(neigh)
                        count += 1
                        count += dfs(neigh[0], neigh[1], visited)
                    visited.remove(neigh)

            mem[(i, j)] = count % 1000000007
            return mem[(i, j)]

        for p in range(m):
            for q in range(n):
                visited = set()
                visited.add((p, q))
                # print("start ",p,q)
                cnt += dfs(p, q, visited)
                # print(p, q, cnt[0])

        # print(dp)
        # count = 0
        # for i in dp:
        #     count += sum(i)
        return (cnt + m * n) % (1000000007)


Solution()

"""
iterative dp
"""


class Solution:
    def countPaths(self, grid) -> int:

        m = len(grid)
        n = len(grid[0])

        def find_neighbour(i, j):
            o = []

            if i + 1 < m:
                o.append((i + 1, j))

            if i - 1 >= 0:
                o.append((i - 1, j))

            if j + 1 < n:
                o.append((i, j + 1))

            if j - 1 >= 0:
                o.append((i, j - 1))

            return o

        dp = [[1] * n for _ in range(m)]

        cells = sorted(
            [
                [i, j] for j in range(n)
                for i in range(m)
            ],
            key=lambda x: grid[x[0]][x[1]]
        )

        for cell in cells:
            for neigh in find_neighbour(cell[0], cell[1]):
                if grid[cell[0]][cell[1]] < grid[neigh[0]][neigh[1]]:
                    dp[neigh[0]][neigh[1]] += dp[cell[0]][cell[1]]
                    dp[neigh[0]][neigh[1]] %= 1000000007

        return sum(sum(row) % 1000000007 for row in dp) % 1000000007


