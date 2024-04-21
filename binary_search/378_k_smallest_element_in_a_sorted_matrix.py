"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

correct heap logic present in golang, this heap code is also accepted but it takes more time than
the open present in golang

"""
import bisect


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        left, right = matrix[0][0], matrix[-1][-1]

        while left < right:
            # eventually end up with the element that exists in the matrix
            mid = left + (right - left) // 2
            count = self.count_less_than_equal_elem(matrix, mid)
            print(left, mid, right, count)  # best to see this print and how low becomes the ans
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    def count_less_than_equal_elem(self, matrix, mid):

        # for each row we calculate how many elements are less than equal to mid
        count = 0
        i = 0
        while i < len(matrix):
            arr = matrix[i]
            count += bisect.bisect_right(arr, mid)
            i += 1

        return count


# a = Solution().kthSmallest([[1,6,10,13,14,16,21],[3,10,12,18,22,27,29],[3,15,19,20,23,29,34],[8,15,19,25,27,29,39],
#                         [12,17,24,25,28,29,41],[16,22,27,31,31,33,44],[20,26,28,35,39,41,45]], 38)

# a = Solution().kthSmallest([[4, 5, 10], [6, 9, 13], [8, 11, 15]], 8)
a = Solution().kthSmallest([[10, 20, 35, 90], [15, 25, 70, 185], [28, 30, 200, 205], [29, 190, 210, 235]], 10)

print(a)
