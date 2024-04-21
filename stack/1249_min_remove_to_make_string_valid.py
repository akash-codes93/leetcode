"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        final = ""

        for i in s:

            if len(stack) == 0 and i not in ["(", ")"]:
                final += i

            elif i == ')':
                if len(stack) == 0:  # ignore case
                    pass
                else:
                    sub_str = ")"

                    while len(stack) > 0 and stack[-1] != "(":
                        val = stack.pop()
                        sub_str += val

                    sub_str += stack.pop()
                    # print(sub_str)

                    if len(stack) == 0:
                        sub_str = sub_str[::-1]
                        final += sub_str
                    else:
                        stack.append(sub_str)
            else:
                stack.append(i)
            # print(stack)

        semi_final = ""

        while len(stack) != 0:
            val = stack.pop()
            if val != "(":
                semi_final += val

        semi_final = semi_final[::-1]

        # print(final + semi_final)
        return final + semi_final


# Solution().minRemoveToMakeValid("lee(t(c)o)de)")
# Solution().minRemoveToMakeValid("a)b(c)d")
# Solution().minRemoveToMakeValid(")))(((")
# Solution().minRemoveToMakeValid("(")
Solution().minRemoveToMakeValid(")")

