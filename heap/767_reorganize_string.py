"""
https://leetcode.com/problems/reorganize-string/
"""
import math


class Node:

    def __init__(self, element, frequency):
        self.element = element
        self.frequency = frequency


def heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = i

    if left < heap_size and arr[left].frequency > arr[largest].frequency:
        largest = left

    if right < heap_size and arr[right].frequency > arr[largest].frequency:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, heap_size)


def increase_key(arr, value):
    arr.append(value)

    i = len(arr) - 1
    while i > 0:
        parent = math.ceil(i / 2) - 1

        if arr[parent].frequency >= arr[i].frequency:
            break

        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def build_heap(arr):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        heapify(arr, i, len(arr))


class Solution:
    def reorganizeString(self, s: str) -> str:
        d = {}

        for i in range(0, len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        arr = []
        print(d)

        for key, value in d.items():
            # print(key, value)
            arr.append(Node(key, value))

        build_heap(arr)

        ans = ""

        while len(arr) > 1:
            val1 = arr[0]
            arr[0] = arr[-1]
            arr.pop()
            heapify(arr, 0, len(arr))

            val2 = arr[0]
            arr[0] = arr[-1]
            arr.pop()
            heapify(arr, 0, len(arr))

            print(val1.element, val2.element)
            ans += val1.element
            val1.frequency -= 1

            ans += val2.element
            val2.frequency -= 1

            if val1.frequency:
                increase_key(arr, val1)

            if val2.frequency:
                increase_key(arr, val2)

        if len(arr) == 1 and arr[0].frequency > 1:
            return ""
        elif len(arr) == 1:
            ans += arr[0].element
            return ans

        return ans


# p = Solution().reorganizeString("aab")
# p = Solution().reorganizeString("aaab")
# p = Solution().reorganizeString("aaabbcccd")
# p = Solution().reorganizeString("a")
# p = Solution().reorganizeString("kkkkzrkatkwpkkkktrq")
# p = Solution().reorganizeString("aaaaabcdq")
# p = Solution().reorganizeString("aabbcc")
p = Solution().reorganizeString("bfrbs")
print("Ans")
print(p)

