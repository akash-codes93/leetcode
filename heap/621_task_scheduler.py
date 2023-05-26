import math


class Node:
    def __init__(self, task, count):
        self.task = task
        self.count = count


def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2

    largest = i
    if left < heap_size and arr[left].count > arr[largest].count:
        largest = left

    if right < heap_size and arr[right].count > arr[largest].count:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, largest, heap_size)


def perculate_up(arr, node):
    arr.append(node)
    i = len(arr) - 1
    while i > 0:
        parent = math.ceil(i / 2) - 1
        if arr[parent].count > arr[i].count:
            break
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def build_heap(arr):

    for i in range(math.floor(len(arr)/2)-1, -1, -1):
        max_heapify(arr, i, len(arr))


class Solution:

    def check_if_task_be_scheduled(self, node, task_mapping, n, current_time):
        if node.task not in task_mapping:
            return True
        elif current_time - task_mapping[node.task] > n:
            return True

        return False

    def leastInterval(self, tasks, n: int) -> int:

        task_count = {}
        for task in tasks:
            p = task_count.get(task, 0)
            task_count[task] = p+1

        arr = []
        for key, value in task_count.items():
            arr.append(
                Node(key, value)
            )

        build_heap(arr)

        current_time = 0
        task_mapping = {}
        order = []
        parr = []

        while arr or parr:
            # print([(i.task, i.count) for i in arr])

            # aprr = []
            print("addition arr: ", [(i.task, i.count) for i in parr])
            while parr:
                node = parr[0]
                print("node to restore:", node.task)
                if current_time - task_mapping[node.task] > n:
                    perculate_up(arr, node)
                    parr.pop(0)
                else:
                    break

            if len(arr) == 0:
                current_time += 1
                order.append("idle")
                continue

            node = arr[0]
            print("To be scheduled: ", node.task)

            possible = self.check_if_task_be_scheduled(node, task_mapping, n, current_time)
            if possible:
                print("scheduled: ", node.task)
                order.append(node.task)
                task_mapping[node.task] = current_time
                node.count -= 1
                arr[0] = arr[-1]
                arr.pop()
                max_heapify(arr, 0, len(arr))
                print([(i.task, i.count) for i in arr])

                if node.count > 0:
                    parr.append(node)
                current_time += 1

            print("---")

        print(order)
        return current_time


# ans = Solution().leastInterval(["A","A","A","B","B","B"], n = 2)
# ans = Solution().leastInterval(["A","A","A","B","B","B"], n = 0)
# ans = Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2)
# ans = Solution().leastInterval(["A","B","C","D","E","A","B","C","D","E"],4)
ans = Solution().leastInterval(["F","J","J","A","J","F","C","H","J","B","E","G","G","F","A","C","I","F","J","C","J","C","H","C","A","D","G","H","B","F","G","C","C","A","E","B","H","J","E","I","F","D","E","A","C","D","B","D","J","J","C","F","D","D","J","H","A","E","C","D","J","D","G","G","B","C","E","G","H","I","D","H","F","E","I","B","D","E","I","E","C","J","G","I","D","E","D","J","C","A","C","C","D","I","J","B","D","H","H","J","G","B","G","A","H","E","H","E","D","E","J","E","J","C","F","C","J","G","B","C","I","I","H","F","A","D","G","F","C","C","F","G","C","J","B","B","I","C","J","J","E","G","H","C","I","G","J","I","G","G","J","G","G","E","G","B","I","J","B","H","D","H","G","F","C","H","C","D","A","G","B","H","H","B","J","C","A","F","J","G","F","E","B","F","E","B","B","A","E","F","E","H","I","I","C","G","J","D","H","E","F","G","G","D","E","B","F","J","J","J","D","H","E","B","D","J","I","F","C","I","E","H","F","E","G","D","E","C","F","E","D","E","A","I","E","A","D","H","G","C","I","E","G","A","H","I","G","G","A","G","F","H","J","D","F","A","G","H","B","J","A","H","B","H","C","G","F","A","C","C","B","I","G","G","B","C","J","J","I","E","G","D","I","J","I","C","G","A","J","G","F","J","F","C","F","G","J","I","E","B","G","F","A","D","A","I","A","E","H","F","D","D","C","B","J","I","J","H","I","C","D","A","G","F","I","B","E","D","C","J","G","I","H","E","C","E","I","I","B","B","H","J","C","F","I","D","B","F","H","F","A","C","A","A","B","D","C","A","G","B","G","F","E","G","A","A","A","C","J","H","H","G","C","C","B","C","E","B","E","F","I","E","E","D","I","H","G","F","A","H","B","J","B","G","H","C","C","B","G","C","B","A","E","G","A","J","G","D","C","I","G","F","G","G","A","J","E","I","D","E","A","F","A","H","C","E","D","D","D","H","I","F","F","A","F","A","A","C","J","D","J","H","I","F","A","C","B","C","A","C","C","H","A","J","I","B","A","I","F","J","C","I","B","C","E","E","E","J","G","F","E","I","A","A","E","B","J","H","H","H","A","H","J","E","F","E","F","G","J","D","I","D","I","F","B","J","D","A","A","D","F","G","B","J","H","F","A","D","H","C","B","A","J","H","I","F","H","E","G","B","A","F","F","A","C","D","G","I","I","J","H","H","C","J","G","B","A","D","B","F","J","D","I","A","F","F","F","F","A","E","B","C","G","H","E","B","B","A","G","D","C","C","E","A","C","F","G","A","I","F","B","H","J","G","C","B","H","D","A","H","B","H","H","C","A","F","I","C","F","A","C","J","I","H","H","F","B","B","D","E","C","J","F","C","E","A","J","E","C","A","E","B","A","J","F","J","J","J","H","H","C","I","E","G","G","H","J","J","H","H","H","J","H","A","G","I","C","E","C","D","G","G","F","H","D","G","H","A","E","I","D","A","H","G","E","A","B","F","I","C","A","F","B","A","I","F","G","I","F","D","A","B","J","B","D","F","G","J","J","A","A","C","H","G","F","B","I","I","J","A","H","D","F","E","F","J","B","F","C","G","E","A","G","H","E","H","H","F","I","G","C","C","G","J","B","H","F","H","D","I","B","D","I","F","H","I","D","F","G","G","E","A","C","A","G","H","G","H","J","F","D","F","G","D","D","C","J","C","J","G","G","G","G","H","H","G","D","E","H","G","C","B","F","I","F","C","H","J","I","A","F","D","C","F","C","E","E","D","D","C","G","B","F","E","J","C","I","E","D","B","B","I","I","I","H","C","E","C","J","F","G","A","I","J","D","I","C","G","F","I","E","I","E","F","A","G","E","J","A","I","A","D","A","G","J","F","E","D","I","A","E","J","I","C","J","B","F","B","E","C","E","F","G","E","J","J","I","E","D","F","C","H","H","B","G","D","I","I","F","B","G","C","F","J","B","G","J","H","D","G","C","C","I","I","E","I","B","H","B","I","G","F","H","G","C","J","D","C","E","G","F","C","H","D","A","C","D","H","B","C","H","I","B","A","J","C","B","D","J","D","H","F","B","A","G","G","J","I","E","F","A","D","H","D","B","C","A","H","F","G","B","F","H","B","H","I","J","D","H","I","B","C","D","G","A","E","A","A","I","F","I","F","B","B","I","F","A","E","I","A","B","G","C","F","I","A","F","I","D","H","B","I","I","B","J","F","E","B","B","B","D","C","J","E","J","J","G","D","F","F","F","G","I","H","J","J","G","D","G","F"],8)

print(ans)

