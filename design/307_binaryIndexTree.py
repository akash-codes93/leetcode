class NumArray:
    # binary indexed tree

    def __init__(self, nums):

        self.nums = nums
        self.bit = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            self.bit_update(idx, num)
            print("--")

        print(self.bit)

    def bit_update(self, i, val):
        i += 1
        while i < len(self.bit):
            print(i)
            self.bit[i] += val
            i += (i & -i)

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        self.bit_update(i, diff)

    def sum(self, i):
        total = 0
        while i > 0:
            print(i)
            total += self.bit[i]
            i -= (i & -i)
        print("---")
        return total

    def sumRange(self, left: int, right: int) -> int:
        return self.sum(right+1) - self.sum(left)


a = NumArray([1, 16, 6, 5, 2, 1, 4, 1, 7])
p = a.sumRange(1, 8)
print(p)
