
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows > len(s) or len(s) == 1:
            return s

        out = ""

        for i in range(numRows):

            substr = ""
            p = i

            while p < len(s):
                substr += s[p]

                p += (2 * numRows) - 2

                if i != 0 and i != numRows-1:
                    if p - (2*i) < len(s):
                        substr += s[p - (2*i)]

            out += substr

        return out

print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("PAYPALISHIRING", 5))

