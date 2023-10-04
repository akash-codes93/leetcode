"""
stack + freq + visited

maintain stack monotonically increasing
if already visited then skip
if freq is 0 cannot pop

decrease frequency

"""


from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(list(s))
        visited = [0] * 26

        for i in range(len(s)):
            idx = ord(s[i]) - 97
            counter[s[i]] -= 1

            if visited[idx] == 1:
                continue

            while len(stack) and counter[stack[-1]] > 0 and stack[-1] >= s[i]:
                val = stack.pop()
                visited[ord(val) - 97] = 0

            visited[idx] = 1
            stack.append(s[i])

        return "".join(stack)


sol = Solution()
sol.removeDuplicateLetters("cbacdcbc")
sol.removeDuplicateLetters("bcabc")
sol.removeDuplicateLetters("abacb")

