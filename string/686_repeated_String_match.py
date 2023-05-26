"""

"""

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        """bad code"""
        p = a
        t = 1
        while len(p) < len(b):
            p += a
            t += 1

        if b in p: return t
        elif b in p+a: return t+1
        return -1


