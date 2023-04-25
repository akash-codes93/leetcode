"""
https://leetcode.com/problems/top-k-frequent-words/
same as k frequent element
one from change -- if frequency is same compare the first char of words
because of this in question
Note that "i" comes before "love" due to a lower alphabetical order.

"""


import math


class Node:

    def __init__(self, elem, freq):
        self.freq = freq
        self.elem = elem


def max_heapify(arr, i, heap_size):
    left = 2*i+1
    right = 2*i+2

    largest = i

    if left < heap_size and arr[left].freq > arr[largest].freq:
        largest = left

    if left < heap_size and arr[left].freq == arr[largest].freq and arr[left].elem < arr[largest].elem:
        largest = left

    if right < heap_size and arr[right].freq > arr[largest].freq:
        largest = right

    if right < heap_size and arr[right].freq == arr[largest].freq and arr[right].elem < arr[largest].elem:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]

        max_heapify(arr, largest, heap_size)



def build_heap(arr):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        max_heapify(arr, i, len(arr))


class Solution:
    def topKFrequent(self, words, k):

        d = {}

        for i in words:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        arr = []
        for p, v in d.items():
            arr.append(Node(p, v))

        build_heap(arr)

        st = []
        p = 1
        for i in range(len(arr) - 1, len(arr) - 1 - k, -1):
            node = arr[0]
            st.append(node.elem)

            arr[i], arr[0] = arr[0], arr[i]

            max_heapify(arr, 0, len(arr) - p)
            p += 1

        return st

# a = Solution().topKFrequent(["i","love","leetcode","i","love",'az', "coding", 'az'], 3)
# a = Solution().topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)
a = Solution().topKFrequent(["a","aa","aaa"], 2)
print(a)