"""
@url: https://leetcode.com/problems/word-search/

for every element you have to call the recursion element.

optimisation instead of storing path we can change the element to .
in this way space complexity will be reduced.
"""
from typing import List


class Solution:

    def get_adjacent_cells(self, board, i, j):

        def check(cell1):
            if board[cell1[0]][cell1[1]] != '.':
                return True
            return False

        output = []
        # up
        cell = (i-1, j)
        if i-1 >= 0 and check(cell):
            output.append(cell)

        # down
        cell = (i+1, j)
        if i+1 < len(board) and check(cell):
            output.append(cell)

        # left
        cell = (i, j-1)
        if j-1 >= 0 and check(cell):
            output.append(cell)

        # right
        cell = (i, j+1)
        if j+1 < len(board[i]) and check(cell):
            output.append(cell)

        return output

    def word_search(self, board, i, j, word, k):

        if k == len(word):
            return True

        if board[i][j] == '.':
            return False

        main_status = False

        if board[i][j] == word[k]:
            print(i,j,k)
            if k == len(word)-1:
                main_status = True
            adjacency = self.get_adjacent_cells(board, i, j)
            for cell in adjacency:
                temp = board[i][j]
                board[i][j] = '.'
                status = self.word_search(board, cell[0], cell[1], word, k+1)
                if status:
                    main_status = status
                board[i][j] = temp

        return main_status

    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[i])):

                if self.word_search(board, i, j, word, 0):
                    return True

        return False



# print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
# print(Solution().exist([["a"]], "a"))
print(Solution().exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","B"],["A","A","A","A","B","A"]], "AAAAAAAAAAAAABB"))

