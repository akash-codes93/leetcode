"""
slower
time: l^2 * n * log(n)
"""
import bisect


class SolutionSlow:
    def ispredecessor(self, s1, s2):
        if len(s2) - len(s1) != 1:
            return False

        # lcs
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        if dp[-1][-1] == len(s1):
            return True
        return False

    def longestStrChain(self, words) -> int:

        words = sorted(words, key=lambda x: len(x))
        len_words = [len(word) for word in words]

        dp = [1] * len(words)
        for i in range(1, len(words)):
            idx = bisect.bisect_left(len_words, len_words[i] - 1)
            for j in range(idx, i):
                if self.ispredecessor(words[j], words[i]) and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1

        print(dp[-1])
        print(dp)
        return max(dp)


"""
Faster
nlog(n) * l
"""


class Solution:

    def longestStrChain(self, words) -> int:

        words = sorted(words, key=lambda x: len(x))
        dp = {}
        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]

                if new_word in dp:
                    dp[word] = max(dp[word], dp[new_word]+1)

        # print(max(dp.values()))
        return max(dp.values())


sol = Solution()
sol.longestStrChain(["a", "b", "ba", "bca", "bda", "bdca"])
sol.longestStrChain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"])
sol.longestStrChain(["abcd", "dbqca"])
sol.longestStrChain(["a", "b", "ab", "bac"])

# print(sol.ispredecessor("abcd", "dbqca"))
