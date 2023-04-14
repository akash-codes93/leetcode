"""
https://leetcode.com/problems/sqrtx/
"""
# class Solution:
#
#     def mySqrt(self, x: int) -> int:
#
#         if x == 1:
#             return 1
#
#         l = 0
#         r = x // 2
#
#         while l <= r:
#             mid = (l + r) / 2
#             print(mid, l, r)
#
#             if mid * mid == x:
#                 return math.floor(mid)
#             elif mid * mid < x:
#                 l = mid
#             else:
#                 r = mid
#         return math.floor(l)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l = 1
        r = x // 2
        while l <= r:
            print(l, r)
            mid = (l + r) // 2

            if mid * mid < x:
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
            else:
                return mid
        return min(l, r)

# print(Solution().mySqrt(17))
# print(Solution().mySqrt(23))
# print(Solution().mySqrt(36))
print(Solution().mySqrt(4))
