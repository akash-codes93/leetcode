import math


class Node:

    def __init__(self, val, idx, segment):
        self.val = val
        self.idx = idx
        self.segment = segment

    def __lt__(self, other):

        if self.val < other.val:
            return True
        elif self.val == other.val and self.idx < other.idx:
            return True

        return False


def min_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    smallest = i
    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left

    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    if i != smallest:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, smallest, heap_size)


def build_heap(arr):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        min_heapify(arr, i, len(arr))


class Solution:
    def totalCost(self, costs, k: int, candidates: int) -> int:

        arr = []
        for idx, i in enumerate(costs):
            arr.append(Node(i, idx, 0))

        heap = []
        n = candidates
        while arr and n > 0:
            node = arr.pop(0)
            node.segment = 1
            heap.append(node)
            n -= 1

        n = candidates
        while arr and n > 0:
            node = arr.pop()
            node.segment = 2
            heap.append(node)
            n -= 1

        build_heap(heap)

        # main logic
        cost = 0

        while k > 0:
            print([(i.idx, i.val) for i in heap])
            node = heap[0]
            print(node.val)
            cost += node.val
            print("arr:", [(i.idx, i.val) for i in arr])
            if arr:
                if node.segment == 1:
                    np = arr.pop(0)
                else:
                    np = arr.pop()
            else:
                np = heap[-1]
                heap.pop()
            print("new_node: ", np.val)
            np.segment = node.segment
            if heap:
                heap[0] = np
            else:
                heap.append(np)
            min_heapify(heap, 0, len(heap))
            k -= 1

        return cost


c = Solution().totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], 11, 2)
print(c)
