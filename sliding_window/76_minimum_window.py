class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_freq = [0] * 58
        t_freq = [0] * 58
        minl = float('inf')
        l, r = 0, 0
        ans = ""

        for i in t:
            t_freq[ord(i)-65] += 1

        def matcher():
            for i in range(58):
                if not(window_freq[i] >= t_freq[i]):
                    return False
            return True

        while r < len(s):
            window_freq[ord(s[r]) - 65] += 1

            if matcher():
                if (r - l + 1) <= minl:
                    minl = (r - l + 1)
                    ans = s[l : r+1]

                while l <= r:
                    l += 1
                    window_freq[ord(s[l-1]) - 65] -= 1
                    if matcher():
                        if (r - l + 1) < minl:
                            minl = (r - l + 1)
                            ans = s[l: r + 1]
                    else:
                        break
            r += 1
        return ans


# print(Solution().minWindow("BABCCA", "AC"))
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
# print(Solution())
# print(Solution())
