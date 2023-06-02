
class Solution1:

    def nextGreaterElement(self, nums1, nums2):

        stack = []
        mapper = {}

        for i in range(len(nums2)-1, -1, -1):

            while stack and stack[-1] < nums2[i]:
                stack.pop()

            if not stack:
                mapper[nums2[i]] = -1
            else:
                mapper[nums2[i]] = stack[-1]

            stack.append(nums2[i])

        return [mapper[i] for i in nums1]


class Solution2:
    def nextGreaterElements(self, nums):

        stack = []
        mapper = []

        nums = nums + nums

        for i in range(len(nums) - 1, -1, -1):

            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if not stack:
                mapper.append(-1)
            else:
                mapper.append(stack[-1])

            stack.append(nums[i])

        mapper.reverse()
        return mapper[:len(nums)]


class Solution:
    def nextGreaterElement(self, n: int) -> int:

        if n < 10:
            return -1
        arr = [int(i) for i in str(n)]
        i = len(arr) - 1
        while i > 0 and arr[i] < arr[i-1]:
            i -= 1

        if i == 0:
            return -1

        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -=1

        arr[i], arr[j] = arr[j], arr[i]
        arr[i+1:] = sorted(arr[i+1:])
        ans = "".join(arr)
        return int(ans) if int(ans) < 2**31 else -1


