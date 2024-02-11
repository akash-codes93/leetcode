"""
https://leetcode.com/problems/remove-invalid-parentheses/
"""
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def check_str_valid(s):
            if len(s) == 0:
                return True

            total = 0
            for i in s:
                if i == '(':
                    total += 1

                if i == ')':
                    total -= 1

                if total < 0:
                    return False

            return total == 0

        max_len = [0]
        main_output = []

        def dfs(s, i):

            if i == len(s):
                if check_str_valid(s) and len(s) >= max_len[0] and s not in main_output:
                    max_len[0] = len(s)
                    main_output.append(s)

                return

            if len(s) < max_len[0]:
                return

            if s[i] not in {'(', ')'}:
                dfs(s, i + 1)
                return

            for p in [0, 1]:
                if p:
                    dfs(s, i + 1)
                else:
                    dfs(s[:i] + s[i + 1:], i)

            return

        dfs(s, 0)
        # print(main_output)
        # print(max_len)
        return list(filter(lambda x: len(x) == max_len[0], main_output))