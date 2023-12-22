"""
https://leetcode.com/problems/design-a-food-rating-system/
hash map of heap
map of food: node
map of food: rating
"""
import math
from typing import List
from collections import defaultdict
# from sortedcontainers import SortedList


class Node:
    def __init__(self, food, cuisine, rating):
        self.food = food
        self.cuisine = cuisine
        self.rating = rating

    def __gt__(self, other):
        if self.rating < other.rating:
            return False
        elif self.rating == other.rating and self.food > other.food:
            return False
        return True


def max_heapify(arr, i, heap_size):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest, len(arr))


def perculate_up(arr, node):
    arr.append(node)
    i = len(arr) - 1

    while i > 0:
        parent = math.ceil(i / 2) - 1
        if arr[parent] > arr[i]:
            break
        arr[parent], arr[i] = arr[i], arr[parent]
        i = parent


def build_heap(arr):
    for i in range(math.floor(len(arr) / 2) - 1, -1, -1):
        max_heapify(arr, i, len(arr))


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisines_map = defaultdict(list)
        self.food_rating = {}

        for i in range(0, len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]

            node = Node(food, cuisine, rating)
            heap = self.cuisines_map[cuisine]
            # sorted_set = self.cuisines_map[cuisine]
            perculate_up(heap, node)
            # sorted_set.add(node)
            self.food_map[food] = node
            self.food_rating[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        node = self.food_map[food]
        # node.rating = newRating
        heap = self.cuisines_map[node.cuisine]
        # sorted_set = self.cuisines_map[node.cuisine]
        # sorted_set.remove(node)
        # sorted_set.add(node)
        newNode = Node(node.food, node.cuisine, newRating)
        perculate_up(heap, newNode)
        self.food_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisines_map[cuisine]
        while len(heap) > 0:
            node = heap[0]
            if node.rating == self.food_rating[node.food]:
                return node.food
            heap[0] = heap[-1]
            heap.pop()
            max_heapify(heap, 0, len(heap))
