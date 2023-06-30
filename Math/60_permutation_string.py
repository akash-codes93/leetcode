"""

"""


class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        nums = [1]

        for i in range(2, n+1):
            fact.append(fact[-1]*i)
            nums.append(i)

        print(fact)
        print(nums)
        ans = ""
        while n > 1:
            index = (k-1) // fact[n-2]
            # print("k, fact[n-2], index, :", k, fact[n-2], index)
            ans += str(nums[index])
            del nums[index]
            k = k - (index * fact[n-2])
            n = n-1

        ans += str(nums[-1])
        return ans


# perm = Solution().getPermutation(3, 5)
perm = Solution().getPermutation(4, 6)
print(perm)
