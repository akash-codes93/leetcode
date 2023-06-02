"""
https://leetcode.com/problems/insert-delete-getrandom-o1/
"""

import random


class RandomizedSetSlow:
    """
    list + set
    use array for random number generation
    and use set for insertion and deletion = time beats 30%
    """

    def __init__(self):
        self.nums = set()
        self.nums_array = []

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.nums.add(val)
        self.nums_array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False
        self.nums.remove(val)
        return True

    def getRandom(self) -> int:

        idx = random.randint(0, len(self.nums_array) - 1)
        if self.nums_array[idx] not in self.nums:
            return self.getRandom()
        return self.nums_array[idx]


class RandomizedSet:
    """
    list + map
    remove copy last event from list and pop the last element
    """

    def __init__(self):
        self.map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.nums.append(val)
        self.map[val] = len(self.nums)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        # pop from map and replace with last element in array and remove last elem [update index in map also]

        self.map[self.nums[-1]] = self.map[val]
        self.nums[self.map[val]] = self.nums[-1]

        self.nums.pop()
        self.map.pop(val)
        return True

    def getRandom(self) -> int:

        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
