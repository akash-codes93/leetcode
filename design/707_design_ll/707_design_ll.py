"""
https://leetcode.com/problems/design-linked-list/description/
can be optimised for insert at index where check if cap == index and use add at tail
"""


class Node:

    def __init__(self, val=0, _next=None, prev=None):
        self.val = val
        self.next = _next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.start = Node(0)
        self.end = Node(0)

        self.start.next = self.end
        self.end.prev = self.start

        self.cap = 0

    def get_node_at_index(self, index):
        tr = self.start
        st = -1
        while st != index:
            tr = tr.next
            st += 1
        return tr

    def delete_node(self, node):
        prev = node.prev
        _next = node.next

        prev.next = _next
        _next.prev = prev

    def insert_to_next(self, node, val):
        new_node = Node(val)
        temp = node.next
        new_node.next = temp
        new_node.prev = node

        node.next = new_node
        temp.prev = new_node

    def get(self, index: int) -> int:
        if index >= self.cap:
            return -1
        node = self.get_node_at_index(index)
        return node.val

    def addAtHead(self, val: int) -> None:
        node = self.get_node_at_index(-1)
        self.insert_to_next(node, val)
        self.cap += 1

    def addAtTail(self, val: int) -> None:
        self.cap += 1
        new_node = Node(val)
        node = self.end.prev
        temp = node.next
        new_node.next = temp
        new_node.prev = node

        node.next = new_node
        temp.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.cap:
            return
        node = self.get_node_at_index(index - 1)
        self.insert_to_next(node, val)
        self.cap += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.cap:
            return
        node = self.get_node_at_index(index)
        self.delete_node(node)
        self.cap -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)