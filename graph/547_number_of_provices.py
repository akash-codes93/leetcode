"""
https://leetcode.com/problems/number-of-provinces/

Technique 1
Union find
"""


class SolutionUF:
    def findCircleNum(self, isConnected) -> int:

        dsuf = [-1] * len(isConnected)

        def find(v):
            if dsuf[v] == -1:
                return v
            return find(dsuf[v])

        def union(to, _from):
            to_p = find(to)
            from_p = find(_from)
            dsuf[to_p] = from_p

        for start in range(isConnected):
            for end in range(isConnected[start]):

                if start == end:
                    continue
                elif isConnected[start][end] == 0:
                    continue
                else:
                    start_parent = find(start)
                    end_parent = find(end)

                    if start_parent == end_parent: continue
                    union(start_parent, end_parent)

        total = 0
        for i in dsuf:
            if i == -1: total += 1

        return total


"""
Technique 2
BFS
"""


class SolutionBFS:
    def findCircleNum(self, isConnected) -> int:
        total = 0
        visited = set()

        for i in range(len(isConnected)):
            if i not in visited:
                # print(i)
                total += 1
                queue = [i]

                visited.add(i)
                while queue:
                    node = queue.pop(0)
                    # print("queue:", node)

                    for j in range(len(isConnected[node])):
                        if node == j:
                            continue
                        elif isConnected[node][j] == 0:
                            continue
                        elif j in visited:
                            continue
                        else:
                            # print("j", j)
                            visited.add(j)
                            queue.append(j)
            # print("--")
        return total


"""
Technique 3
DFS
"""


class SolutionDFS:
    def findCircleNum(self, isConnected) -> int:
        total = 0
        visited = set()

        def dfs(node):
            for j in range(len(isConnected[node])):
                if node == j:
                    continue
                elif isConnected[node][j] == 0:
                    continue
                elif j in visited:
                    continue
                else:
                    visited.add(j)
                    dfs(j)

        for i in range(len(isConnected)):
            if i not in visited:
                total += 1
                dfs(i)

        return total

