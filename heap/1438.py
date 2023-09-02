class Node:

    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

    def __gt__(self, other):
        if (self.val > other.val) or ((self.val == other.val) and (self.idx > other.idx)):
            return True
        return False


def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = i
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, heap_size)


def min_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left

    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest, heap_size)


def max_perculate_up(arr, val):
    arr.append(val)
    i = len(arr) - 1
    while i > 0:
        parent = math.ceil(i / 2) - 1

        if arr[parent] > arr[i]:
            break

        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def min_perculate_up(arr, val):
    arr.append(val)
    i = len(arr) - 1
    while i > 0:
        parent = math.ceil(i / 2) - 1

        if arr[parent] < arr[i]:
            break

        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        min_heap = []
        max_heap = []

        l = 0
        r = 0
        max_len = 0

        while l <= r < len(nums):
            min_perculate_up(min_heap, Node(nums[r], r))
            max_perculate_up(max_heap, Node(nums[r], r))

            if max_heap[0].val - min_heap[0].val <= limit:
                max_len = max(max_len, r - l + 1)
            else:

                if nums[r] == min_heap[0].val:
                    heap = max_heap
                    heapify = max_heapify
                    op_heap = min_heap
                else:
                    heap = min_heap
                    heapify = min_heapify
                    op_heap = max_heap

                while True:
                    if not heap:
                        break

                    val, pos = heap[0].val, heap[0].idx
                    # print("val, pos", val, pos)
                    if pos < l or abs(val - op_heap[0].val) > limit:
                        heap[0] = heap[-1]
                        heap.pop()
                        # print("before heap", [(h.val, h.idx) for h in heap])
                        heapify(heap, 0, len(heap))
                        # print("heap", [(h.val, h.idx) for h in heap])
                        if pos >= l:
                            l = pos + 1
                        continue

                    max_len = max(max_len, r - l + 1)
                    break
            # print(l, r)
            r += 1
        return max_len


Solution().longestSubarray([4,2,2,2,4,4,2,2], 0)

