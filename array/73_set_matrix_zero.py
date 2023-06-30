"""
Inplace

I hate this question took me forever to reduce the space complexity

"""


class Solution:
    def setZeroes(self, grid) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:

                    if grid[0][j] == None or grid[i][0] == None:
                        continue

                    if grid[0][j] in [float('inf'), None]:
                        grid[0][j] = None
                    else:
                        grid[0][j] = float('-inf')  # column

                    if grid[i][0] in [float('-inf'), None]:
                        grid[i][0] = None
                    else:
                        grid[i][0] = float('inf')  # row

        print(grid)
        # applying
        for i in range(m):
            for j in range(n):
                # check row
                if grid[i][0] in [float('inf'), None] and grid[i][j] not in [float('inf'), None, float('-inf')]:
                    grid[i][j] = 0

                # check column
                if grid[0][j] in [float('-inf'), None] and grid[i][j] not in [float('-inf'), None, float('inf')]:
                    grid[i][j] = 0

        print(grid)

# Solution().setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]])
# Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])
Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
# Solution().setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])



