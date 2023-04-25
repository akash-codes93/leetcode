"""
https://leetcode.com/problems/find-median-from-data-stream/description/

approach: use two heaps min and max heap
min heap and max heap has difference of one.

"""
import math


class MedianFinder:

    def __init__(self):

        self.min_heap = []
        self.max_heap = []

    def min_heapify(self, i):
        left = 2*i +1
        right = 2*i+2

        smallest = i

        if left < len(self.min_heap) and self.min_heap[left] < self.min_heap[smallest]:
            smallest =left

        if right < len(self.min_heap) and self.min_heap[right] < self.min_heap[smallest]:
            smallest = right

        if smallest != i:
            self.min_heap[smallest], self.min_heap[i] = self.min_heap[i], self.min_heap[smallest]
            self.min_heapify(smallest)

    def max_heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2

        largest = i

        if left < len(self.max_heap) and self.max_heap[left] > self.max_heap[largest]:
            largest = left

        if right < len(self.max_heap) and self.max_heap[right] > self.max_heap[largest]:
            largest = right

        if largest != i:
            self.max_heap[largest], self.max_heap[i] = self.max_heap[i], self.max_heap[largest]
            self.max_heapify(largest)


    def min_perculate_up(self, num):

        self.min_heap.append(num)
        i = len(self.min_heap) -1
        while i > 0:
            parent = math.ceil(i/2) - 1

            if self.min_heap[parent] < self.min_heap[i]:
                break

            self.min_heap[parent], self.min_heap[i] = self.min_heap[i], self.min_heap[parent]
            i = parent

    def max_perculate_up(self, num):
        self.max_heap.append(num)
        i = len(self.max_heap) - 1
        while i > 0:
            parent = math.ceil(i / 2) - 1

            if self.max_heap[parent] > self.max_heap[i]:
                break

            self.max_heap[parent], self.max_heap[i] = self.max_heap[i], self.max_heap[parent]
            i = parent


    def addNum(self, num: int) -> None:
        print(num)
        print(self.min_heap)
        print(self.max_heap)

        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            self.max_perculate_up(num)
            return

        if len(self.min_heap) == len(self.max_heap):
            if num > self.min_heap[0]:
                self.max_perculate_up(self.min_heap[0])
                print(self.max_heap)
                self.min_heap[0] = num
                self.min_heapify(0)
            else:
                self.max_perculate_up(num)
            return

        if len(self.max_heap) - len(self.min_heap) == 1:
            if num < self.max_heap[0]:
                self.min_perculate_up(self.max_heap[0])
                self.max_heap[0] = num
                self.max_heapify(0)
            else:
                self.min_perculate_up(num)
                return

    def findMedian(self) -> float:

        if len(self.min_heap) == len(self.max_heap):
            print((self.max_heap[0] + self.min_heap[0]) /2)
            return (self.max_heap[0] + self.min_heap[0]) /2
        else:
            print(self.max_heap[0])
            return self.max_heap[0]


obj = MedianFinder()
obj.addNum(1)
obj.findMedian()
obj.addNum(2)
obj.findMedian()
obj.addNum(3)
obj.findMedian()
obj.addNum(4)
obj.findMedian()
obj.addNum(5)
obj.findMedian()
obj.addNum(6)
obj.findMedian()
obj.addNum(7)
obj.findMedian()
obj.addNum(8)
obj.findMedian()
obj.addNum(9)
obj.findMedian()
obj.addNum(10)
obj.findMedian()


