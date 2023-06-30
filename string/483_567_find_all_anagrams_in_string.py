"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

maintain two hashes
one for p and other for sliding s
if hashes match they are anagrams

"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        h1 = [0 ] *26
        k = len(p)

        for i in p:
            idx = ord(i) - 97
            h1[idx] += 1

        ans = []

        i = 0
        j = i
        h2 = [0] *26
        while i <= len(s ) -k and j < len(s):
            # print(j)
            idx = ord(s[j]) - 97
            h2[idx] += 1
            # print("len:", j- i + 1)
            if ( j- i + 1) == k:
                # print("here")
                if h1 == h2:
                    ans.append(i)
                idx = ord(s[i]) - 97
                h2[idx] -= 1
                i += 1
                j += 1
            else:
                j += 1

        return ans
"""

567 is also the same code no change at all
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        h1 = [0] *26
        k = len(s1)

        for i in s1:
            idx = ord(i) - 97
            h1[idx] += 1

        ans = []

        i = 0
        j = i
        h2 = [0] *26
        while i <= len(s2) -k and j < len(s2):
            # print(j)
            idx = ord(s2[j]) - 97
            h2[idx] += 1
            # print("len:", j- i + 1)
            if ( j- i + 1) == k:
                # print("here")
                if h1 == h2:
                    return True
                idx = ord(s2[i]) - 97
                h2[idx] -= 1
                i += 1
                j += 1
            else:
                j += 1

        return False
