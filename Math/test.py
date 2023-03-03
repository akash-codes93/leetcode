# from typing import List
#
# def countSubarrays(nums: List[int], k: int):
#     count = 0
#     i,j=0,0
#     n = len(nums)
#     sum = 0
#     while j< n:
#         sum = nums[j]
#         while (j-i + 1) >= k:
#             sum -= nums[i]
#             i += 1
#
#             count += 1
#         j += 1
#
#     return count
#
# print(countSubarrays([1,2,3,4],3))

# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])

# class Glove:
#     def __init__(self, color):
#         self.__color = color
#
#     def get_color(self):
#         return self.__color
#
# class Second:
#
#     def __init__(self, glove):
#         self.__glove = glove
#
#     def get_glove(self):
#         return self.__glove
#
#
# red_glove = Glove("Red")
# alice = Second(red_glove)
#
#
# print(alice.get_glove().get_color())


# numbers = (1,2,3,4,5,6,7,8,9)
# count_odd, count_even, i = 0,0,0
# while i < len(numbers):
#     print(numbers[i], i, numbers[i]%2)
#     if not numbers[i] % 2:
#         count_even += 1
#     else:
#         count_odd += 1
#     i += 1
#
# print(count_even)
# print(count_odd)

# class A:
#     def __init__(self, x=3):
#         self._x = x
#
#
# class B(A):
#     def __init__(self):
#         super().__init__(5)
#
#     def display(self):
#         print(self._x)
#
#
# def main():
#     obj = B()
#     obj.display()
#
# main()

# A = ("Python", "Java")
# print(type(A))
#
# B = ("Python",)
# print(type(B))
#
# C = ("Python")
# print(type(C))


x = ("b", "a", "c", "a")
y = ["b", "a", "c", "a"]

x.append(4)
y.append(4)
print(x, y)

