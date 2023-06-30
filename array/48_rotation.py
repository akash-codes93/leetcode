"""
180
i, j  - n-i-1, n-j-1
"""

grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = 3

for i in range(n // 2):
    for j in range(n):
        temp = grid[i][j]
        grid[i][j] = grid[n - i - 1][n - j - 1]
        grid[n - i - 1][n - j - 1] = temp

if n & 1:
    grid[n // 2].reverse()

print(grid)

"""
270

transpose -> swap rows(i, j) -> (n-1-i, j)

"""

grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
m = 3
n = 4

g1 = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        g1[i][j] = grid[j][i]

for i in range(n // 2):
    for j in range(m):
        temp = g1[i][j]
        g1[i][j] = g1[n - i - 1][j]
        g1[n - i - 1][j] = temp

print(g1)
