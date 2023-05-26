
class Solution:
    # def repeatedSubstringPattern(self, s: str) -> bool:
    #
    #     for i in range(1, len(s)):
    #         substr = s[:i]
    #
    #         j = i
    #         status = True
    #         while j < len(s):
    #
    #             if substr != s[j: j+i]:
    #                 status = False
    #                 break
    #
    #             j = j+i
    #
    #         if status:
    #             return True
    #
    #     return False

    def repeatedSubstringPattern(self, s: str) -> bool:
        """Not intuitive"""
        """
        Reason: s+s has twice the string of s
        now if we cut some part of first s[1:]  and some part of second s[:-1]
        and check if s exists then we can say that s has a repeated substring pattern
        
        """
        return s in (s+s)[1:-1]


ans = Solution().repeatedSubstringPattern("abab")
# ans = Solution().repeatedSubstringPattern("abcdabcabcabc")
print(ans)