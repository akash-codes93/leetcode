"""
https://leetcode.com/problems/flipping-an-image/
"""


class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(image)
        for i in range(0, n):
            for j in range((n+1)//2):
                k = image[i][j]
                image[i][j] = 1 - image[i][n-j-1]
                image[i][n-j-1] = 1- k

        return image


p = Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
print(p)
