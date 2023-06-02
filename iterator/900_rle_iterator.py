class Node:
    def __init__(self, val, count):
        self.val = val
        self.count = count


class RLEIterator:

    def __init__(self, encoding):

        self.arr = []

        for i in range(0, len(encoding), 2):
            if encoding[i] > 0:
                self.arr.append(Node(encoding[i + 1], encoding[i]))

        self.j = 0

    def next(self, n: int) -> int:
        if len(self.arr) == 0:
            return -1
        p = None
        while n != 0:
            if len(self.arr) == 0:
                return -1
            node = self.arr[0]
            if n > node.count:
                n -= node.count
                p = node.val
                self.arr.pop(0)
            else:
                node.count -= n
                p = node.val
                if node.count == 0:
                    self.arr.pop(0)
                return p

        return p

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)