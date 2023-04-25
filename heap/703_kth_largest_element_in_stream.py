"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

two array of size
N-K and K is maintained
K array is min heap so we get kth largest in O(1) time.
trick an element greater than min of k array comes min_elemnt (of k array) goes to
n-k array

"""
import math


def perculate_up(arr, num):
    arr.append(num)
    i = len(arr) - 1
    while i > 0:
        parent = math.ceil(i / 2) - 1
        if arr[parent] < arr[i]:
            break
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    smallest = i

    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left

    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, smallest, heap_size)


class KthLargest:

    def __init__(self, k: int, nums):
        self.nk_array = []
        self.k_array = []
        self.k = k

        for i in range(0, len(nums)):
            if len(self.k_array) < k:
                perculate_up(self.k_array, nums[i])
            else:
                if self.k_array[0] < nums[i]:
                    self.nk_array.append(self.k_array[0])
                    self.k_array[0] = nums[i]

                    heapify(self.k_array, 0, len(self.k_array))
                else:
                    self.nk_array.append(nums[i])

    def add(self, val: int) -> int:
        if len(self.k_array) < self.k:
            perculate_up(self.k_array, val)
        else:
            if self.k_array[0] < val:
                self.nk_array.append(self.k_array[0])
                self.k_array[0] = val

                heapify(self.k_array, 0, len(self.k_array))
            else:
                self.nk_array.append(val)

        return self.k_array[0]


obj = KthLargest(3, [])
# obj = KthLargest(3, [7, 4, 3, 7, 3, 4, 5])
l = obj.add(10)
l = obj.add(9)
l = obj.add(13)
print(l)
