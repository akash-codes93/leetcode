"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

build a min heap instead of max
and maintain only k elements [first k push directly]

for new element check with top element if that is element is greater it will not push
else it will push


"""
import math


class Node:

    def __init__(self, var1, var2, sum):
        self.var1 = var1
        self.var2 = var2
        self.sum = sum


def heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = i

    if left < heap_size and arr[left].sum > arr[largest].sum:
        largest = left

    if right < heap_size and arr[right].sum > arr[largest].sum:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, len(arr))


def build_heap(arr):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        heapify(arr, i, len(arr))


def perculate_up(arr, elem):
    arr.append(elem)

    i = len(arr) - 1

    while i > 0:

        parent = math.ceil(i / 2) - 1

        if arr[parent].sum > arr[i].sum:
            break

        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


class Solution:

    def kSmallestPairs(self, nums1, nums2, k):

        arr = []

        for i in range(0, min(k, len(nums1))):
            for j in range(0, min(k, len(nums2))):

                if len(arr) < k:
                    perculate_up(arr, Node(nums1[i], nums2[j], nums1[i]+nums2[j]))
                else:
                    if (nums1[i] + nums2[j]) > arr[0].sum:
                        break
                    else:
                        arr[0] = Node(nums1[i], nums2[j], nums1[i]+nums2[j])
                        heapify(arr, 0, len(arr))
        ans = []
        while arr:
            ans.append([arr[0].var1, arr[0].var2])
            arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
            arr.pop()
            heapify(arr, 0, len(arr))

        ans.reverse()
        return ans

        # basic algo T O(klog(m+n))

        #         arr.append(
        #             Node(nums1[i], nums2[j], nums1[i] + nums2[j])
        #         )
        #
        # build_heap(arr)
        #
        # ans = []
        # print([(i.var1, i.var2, i.sum) for i in arr])
        # for i in range(len(arr) - 1, len(arr) - k - 1, -1):
        #     ans.append((arr[0].var1, arr[0].var2))
        #
        #     arr[0], arr[i] = arr[i], arr[0]
        #     arr.pop()
        #
        #     if len(arr) == 0:
        #         break
        #
        #     heapify(arr, 0, len(arr))
        #
        # return ans


if __name__ == "__main__":
    # a = Solution().kSmallestPairs(
    #     [1, 1, 2],
    #     [1, 2, 3],
    #     2
    # )

    # a = Solution().kSmallestPairs(
    #     [1, 2],
    #     [3],
    #     3
    # )

    a = Solution().kSmallestPairs(
        [3, 5, 11],
        [2, 5, 6],
        3
    )


    print(a)
