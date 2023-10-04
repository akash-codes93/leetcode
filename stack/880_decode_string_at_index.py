class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        digits = "123456789"
        total_length = 0
        i = 0
        while total_length < k:

            if s[i] in digits:
                total_length = int(s[i]) * total_length
            else:
                total_length += 1
            i += 1

        for j in range(i - 1, -1, -1):
            char = s[j]
            if char.isdigit():
                total_length //= int(char)
                k %= total_length
            else:
                if k == 0 or k == total_length:
                    return char
                total_length -= 1


if __name__ == "__main__":
    sol = Solution()
    sol.decodeAtIndex("leet2code3", 8)
