class Solution:
    def pacificAtlantic(self, heights):
        # optimised

        # lets do a reverse traversal
        # meaning start from node which are already touch atlanta and from there where we can reach
        m = len(heights)
        n = len(heights[0])

        def get_neighbour(p, q):
            o = []
            if p + 1 < m and heights[p + 1][q] >= heights[p][q]:
                o.append((p + 1, q))

            if p - 1 >= 0 and heights[p - 1][q] >= heights[p][q]:
                o.append((p - 1, q))

            if q - 1 >= 0 and heights[p][q - 1] >= heights[p][q]:
                o.append((p, q - 1))

            if q + 1 < n and heights[p][q + 1] >= heights[p][q]:
                o.append((p, q + 1))

            return o

        def check_reverse_flow(queue):

            visited = set([i for i in queue])
            while queue:

                node = queue.pop(0)

                for neigh in get_neighbour(node[0], node[1]):
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append(neigh)

            return visited

        pacific_queue = []
        atlantic_queue = []

        for i in range(m):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, n - 1))

        for i in range(n):
            pacific_queue.append((0, i))
            atlantic_queue.append((m - 1, i))

        v1 = check_reverse_flow(pacific_queue)
        v2 = check_reverse_flow(atlantic_queue)

        return v1.intersection(v2)