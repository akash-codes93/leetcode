"""
floyd warshall + bit[is used to maintain state] + dp
"""


class Solution:

    def dfs(self, i, dist, mask, dp):
        # all nodes are visited
        if mask == 0:
            return 0

        if (i, mask) in dp:
            return dp[(i, mask)]

        shortest = float('inf')
        for j in range(0, len(dist)):
            # let's check is j is visited or not :: for this we check jth bit is marked 0 or not
            jth_bit = mask & (1 << j)
            if jth_bit:
                # mark j as visited
                path = self.dfs(j, dist, mask ^ (1 << j), dp) + dist[i][j]
                shortest = min(shortest, path)

        dp[(i, mask)] = shortest
        return shortest

    def shortestPathLength(self, graph) -> int:
        n = len(graph)
        # floyd warshall
        dist = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            # distance from same node to node
            dist[i][i] = 0
            # rest all edges have length 1
            for j in range(0, len(graph[i])):
                dist[i][graph[i][j]] = 1

        # calculating all pairs shortest path
        for k in range(0, n):
            for i in range(0, n):
                for j in range(0, n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        shortest_path = float('inf')
        dp = {}
        for i in range(0, n):
            mask = (1 << n) - 1  # n=4; mask = 1111
            # mask ^ (1 << i) : marking ith node as visited.
            path = self.dfs(i, dist, mask ^ (1 << i), dp)
            shortest_path = min(shortest_path, path)

        return shortest_path

