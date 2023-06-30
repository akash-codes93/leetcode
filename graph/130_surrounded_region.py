"""
https://leetcode.com/problems/surrounded-regions/
"""


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        def check_boundary(p, q):

            if p == m - 1 or q == n - 1 or p == 0 or q == 0:
                return True
            return False

        def get_neighbour(p, q):
            out = []
            if p - 1 >= 0 and board[p - 1][q] != 'X':
                out.append((p - 1, q))

            if p + 1 < m and board[p + 1][q] != 'X':
                out.append((p + 1, q))

            if q - 1 >= 0 and board[p][q - 1] != 'X':
                out.append((p, q - 1))

            if q + 1 < n and board[p][q + 1] != 'X':
                out.append((p, q + 1))

            return out

        visited = set()
        for i in range(m):
            for j in range(n):

                if board[i][j] == 'O' and (i, j) not in visited:

                    visited.add((i, j))
                    queue = [(i, j)]
                    path = [(i, j)]
                    status = True

                    while queue:
                        node = queue.pop(0)
                        print(node, check_boundary(*node))
                        if check_boundary(*node):
                            status = False

                        for neigh in get_neighbour(*node):
                            if neigh not in visited:
                                visited.add(neigh)
                                queue.append(neigh)
                                path.append(neigh)

                    print(status, i, j)
                    if status:
                        for t in path:
                            board[t[0]][t[1]] = 'X'


b = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
Solution().solve(b)
print(b)
