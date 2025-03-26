"""
https://leetcode.com/problems/decode-string/description/

use stacks
use '[' as delimeter to separate repeat str
use ']' to calculate string

"""


class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        nums = "0123456789"
        for i in s:
            if i != "]":
                stack.append(i)
            elif i == "]":
                temp_str = ""
                num = ""
                while stack and stack[-1] not in nums and stack[-1] != "[":
                    temp_str = stack.pop() + temp_str

                if stack and stack[-1] == '[':
                    stack.pop()

                while stack and stack[-1] in nums and stack[-1] != "[":
                    num = stack.pop() + num

                if stack and stack[-1] == '[':
                    stack.pop()

                if num:
                    temp_str = int(num) * temp_str

                stack.append(temp_str)

            print(stack)

        out = ""
        while stack:
            out = stack.pop() + out

        return out
