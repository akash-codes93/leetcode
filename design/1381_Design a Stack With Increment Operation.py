"""
push O(1)
pop O(1)
increment O(k)
very easy question not sure why it is medium
"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = [None] * maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size == self.maxSize:
            return
        self.stack[self.size] = x
        self.size += 1


    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        val = self.stack[self.size]
        return val

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i == self.size:
                break
            self.stack[i] += val


