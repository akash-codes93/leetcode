class Solution:
    def longestSubarrayDivK(self, arr, k):

        # Complete the function
        freq = {0: -1}

        max_len = 0
        _sum = 0

        for pos, i in enumerate(arr):
            _sum += i

            rem = _sum % k

            if rem in freq:
                # print(rem, pos, freq, pos - freq[rem], max_len)
                max_len = max(max_len, pos - freq[rem])
            else:
                freq[rem] = pos

        return max_len


print(Solution().longestSubarrayDivK([2, 7, 6, 1, 4, 5], 3))
print(Solution().longestSubarrayDivK([4,5,0,-2,-3,1], 5))