"""
https://leetcode.com/problems/binary-watch/
draw recursion tree very helpful
"""


class Solution:

    def calculate_time(self, arr):

        hr = 0

        for i in range(0, 4):
            hr += arr[i] * 2**i

        mins = 0
        for j in range(4, len(arr)):
            mins += arr[j] * 2**(j - 4)

        if mins < 10:
            mins = '0' + str(mins)

        return str(hr) + ':' + str(mins)

    def validate(self, arr):
        hr = 0

        for i in range(0, 4):
            hr += arr[i] * 2 ** i

        if hr > 11:
            return False

        mins = 0
        for j in range(4, len(arr)):
            mins += arr[j] * 2 ** (j - 4)

        if mins > 59:
            return False

        return True



    def readBinaryWatch(self, turnedOn):
        possible = []

        def helper(arr, to, k):

            if to ==0:
                if not self.validate(arr):
                    return
                possible.append(self.calculate_time(arr))
                return

            if not self.validate(arr):
                return

            for j in range(k, len(arr)):
                arr[j] = 1
                helper(arr, to-1, j+1)
                arr[j] = 0


        helper([0]*10, turnedOn, 0)
        return possible


p = Solution().readBinaryWatch(1)
print(p)