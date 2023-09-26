from collections import Counter


class Node:

    def __init__(self, char, index):
        self.char = char
        self.index = index

    def __str__(self):
        return f"{self.char},{self.index}"


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        nsr = []
        ngr = []

        stack = []
        stack2 = []

        for i in range(len(s)-1, -1, -1):
            while len(stack) and stack[-1].char < s[i]:
                stack.pop()

            if len(stack) == 0:
                nsr.append(None)
                stack.append(Node(s[i], i))
            else:
                nsr.append(stack[-1])
                if stack[-1].char != s[i]:
                    stack.append(Node(s[i], i))

            while len(stack2) and stack2[-1].char >= s[i]:
                stack2.pop()

            if len(stack2) == 0:
                ngr.append(None)
                stack2.append(Node(s[i], i))
            else:
                ngr.append(stack2[-1])
                if stack2[-1].char != s[i]:
                    stack2.append(Node(s[i], i))

            stack2.append(Node(s[i], i))

        nsr = nsr[::-1]
        ngr = ngr[::-1]
        print([str(k) for k in nsr])
        print([str(k) for k in ngr])

        min_stack= []
        for i in range(0, len(s)):
            if nsr[i] is None:
                min_stack.append(ngr[i])
            elif ngr[i] is None:
                min_stack.append(nsr[i])
            else:
                if nsr[i].index < ngr[i].index:
                    min_stack.append(nsr[i])
                else:
                    min_stack.append(ngr[i])

        covered = [None] * 26
        counter = Counter(list(s))
        out = ""
        for idx, i in enumerate(s):
            if covered[ord(i) - 97] != None:
                continue

            elif counter[i] == 1:
                out += i
                covered[ord(i) - 97] = 1
            else:
                min_val = min_stack[idx]
                if min_val != None and min_val.char > i:
                    out += i
                    covered[ord(i) - 97] = 1
                    counter[i] -= 1
                else:
                    counter[i] -= 1

        print(out)
        return out

sol = Solution()
sol.removeDuplicateLetters("cbacdcbc")
sol.removeDuplicateLetters("bcabc")
sol.removeDuplicateLetters("abacb")









