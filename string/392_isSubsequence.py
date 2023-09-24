
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        elif s != "" and t == "":
            return False

        i = 0
        j = 0

        while j < len(t):
            if s[i] == t[j]:
                j += 1
                i += 1
            else:
                j += 1

            if i == len(s):
                break

        if i == len(s):
            return True
        return False







