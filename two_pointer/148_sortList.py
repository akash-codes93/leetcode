"""
https://leetcode.com/problems/sort-list/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head):
    traversal = head
    while traversal:
        print(traversal.val)
        traversal = traversal.next
    print("######################")


class Solution:
    """
    Trying to implement selection sort on linked list
    """
    def node_at_index(self, index, head):
        traversal = head
        position = 0
        while position != index:
            traversal = traversal.next
            position += 1
        return traversal

    def length_of_linked_list(self, head: Optional[ListNode]):
        count = 0
        traversal = head
        while traversal is not None:
            traversal = traversal.next
            count += 1
        return count

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        max_count = self.length_of_linked_list(head) - 1
        while max_count >= 0:
            find_max = float('-inf')
            find_max_node = head
            count = 0
            traversal = head
            while count <= max_count:
                if traversal.val > find_max:
                    find_max = traversal.val
                    find_max_node = traversal

                traversal = traversal.next
                count += 1

            # print("find_max - ", find_max)
            node_at_max = self.node_at_index(max_count, head)
            k = node_at_max.val
            node_at_max.val = find_max
            find_max_node.val = k
            max_count -= 1

        return head


l6 = ListNode(4)
l5 = ListNode(2, l6)
l4 = ListNode(1, l5)
l3 = ListNode(3, l4)
# l2 = ListNode(8, l3)
# l1 = ListNode(5, l2)

print_linked_list(None)

Solution().sortList(None)

print_linked_list(None)

