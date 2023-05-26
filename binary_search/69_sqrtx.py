"""
https://leetcode.com/problems/sqrtx/
https://leetcode.com/problems/valid-perfect-square/
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


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1:
            return True

        l = 0
        r = num // 2

        while l <= r:

            mid = l + (r-l)//2
            temp =mid * mid

            if temp == num:
                return True
            elif temp > num:
                r = mid-1
            else:
                l = mid + 1

        return False

