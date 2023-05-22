"""
using stacks o(h)
"""


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []

        # using stacks O(h) space
        self.stack = []
        tr = root
        self.travel_left(tr)

    def travel_left(self, node):
        while node != None:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        self.travel_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False

"""
using morris traversal
"""


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nodes = []

        tr = root
        while tr != None:
            if tr.left is None:
                self.nodes.append(tr.val)
                tr = tr.right
            else:
                prev = tr
                tr = tr.left
                while tr.right != None and tr.right != prev:
                    tr = tr.right

                if tr.right == prev:
                    self.nodes.append(prev.val)
                    tr.right = None
                    tr = prev.right
                else:
                    tr.right = prev
                    tr = prev.left
        self.i = 0

    def next(self) -> int:
        p = self.i
        self.i += 1
        return self.nodes[p]

    def hasNext(self) -> bool:
        if self.i < len(self.nodes):
            return True
        return False
