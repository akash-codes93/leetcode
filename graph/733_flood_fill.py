"""
https://leetcode.com/problems/flood-fill/
"""


class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):

        m = len(image)
        n = len(image[0])
        org = image[sr][sc]

        def get_neighbours(nd, org):
            out = []
            i = nd[0]
            j = nd[1]

            if i - 1 >= 0 and image[i - 1][j] == org:
                out.append((i - 1, j))
            if i + 1 < m and image[i + 1][j] == org:
                out.append((i + 1, j))
            if j - 1 >= 0 and image[i][j - 1] == org:
                out.append((i, j - 1))
            if j + 1 < n and image[i][j + 1] == org:
                out.append((i, j + 1))

            return out

        queue = [(sr, sc)]
        visited = {(sr, sc)}

        while queue:

            node = queue.pop(0)
            image[node[0]][node[1]] = color

            for neighbour in get_neighbours(node, org):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return image
