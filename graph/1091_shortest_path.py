def find_adjacent_nodes(m, n, final):
    cells = []
    p = [-1, 0, 1]
    q = [-1, 0, 1]

    for i in p:
        for j in q:
            if i == 0 and j == 0:
                continue

            m1 = m + i
            n1 = n + j

            if final[0] >= m1 >= 0 and final[1] >= n1 >= 0:
                cells.append([m1, n1])

    return cells


class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        if grid[0][0] == 1:
            return -1

        final = (len(grid) - 1, len(grid[0]) - 1)

        queue = [[0, 0, 1]]
        visited = {(0, 0)}
        min_dist = float('inf')

        while queue:
            node = queue.pop(0)

            if (node[0], node[1]) == final:
                min_dist = min(node[-1], min_dist)

            new_dist = node[-1] + 1
            adjacent_nodes = find_adjacent_nodes(node[0], node[1], final)

            for each_cell in adjacent_nodes:
                if (each_cell[0], each_cell[1]) not in visited and grid[each_cell[0]][each_cell[1]] != 1:
                    visited.add((each_cell[0], each_cell[1]))
                    each_cell.append(new_dist)
                    queue.append(each_cell)

        if min_dist == float('inf'):
            return -1
        return min_dist
