"""
classical prefix sum question

formula

prefix - k*n = p
p should exists in prefix sum

Also prefix - k*n >=0

so n should from 0 till (prefix - k*n) is positive
"""


class SolutionOK:
    def checkSubarraySum(self, nums, k: int) -> bool:

        prefix_sum = {0: -1}
        total = 0

        for idx, i in enumerate(nums):
            total += i
            t = total
            # n = 0
            n = t//k

            while n >= 0:   # this is right but gives tle...so instead we will go high to low t/k >= n

                p = t-(k*n)
                if p in prefix_sum:
                    length = idx - prefix_sum[p]
                    if length >= 2:
                        return True

                n -= 1

            if total not in prefix_sum:
                prefix_sum[total] = idx

        return False


class SolutionBetter:
    def checkSubarraySum(self, nums, k: int) -> bool:

        prefix_sum = {0: -1}
        total = 0

        for idx, i in enumerate(nums):
            total += i
            remainder = total % k

            if remainder not in prefix_sum:
                prefix_sum[remainder] = idx
            else:
                length = idx - prefix_sum[remainder]
                if length >= 2:
                    return True

        return False

