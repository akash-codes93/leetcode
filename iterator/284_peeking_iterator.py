"""
https://leetcode.com/problems/peeking-iterator/description/
"""


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.queue = []

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        element = self.iterator.next()
        self.queue.append(element)
        return element

    def next(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.pop(0)
        element = self.iterator.next()
        return element

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.queue:
            return True

        return self.iterator.hasNext()