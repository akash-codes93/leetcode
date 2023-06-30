"""
arr = [9,4,9,4,4]
seq = [9, 4]
o/p = 5
"""


# def countAll(arr, seq):
#     count = [0]
#
#     def dfs(i, j):
#         if j == len(seq):
#             print(i, j)
#             count[0] += 1
#             return
#
#         if i == len(arr):
#             return
#
#         if arr[i] == seq[j]:
#             dfs(i + 1, j + 1)
#
#         dfs(i + 1, j)
#
#     dfs(0, 0)
#     print(count[0])


# trying memoization
def countAll(arr, seq):
    # count = [0]

    mem = {}

    def dfs(i, j):

        if (i, j) in mem:
            return mem[(i, j)]

        if j == len(seq):
            print(i, j)
            return 1

        if i == len(arr):
            return 0
        count = 0
        if arr[i] == seq[j]:
            count += dfs(i + 1, j + 1)

        count += dfs(i + 1, j)

        mem[(i, j)] = count

        return count

    c = dfs(0, 0)
    print(c)


countAll([9, 4, 9, 4, 4], [9, 4])


# bottom up

