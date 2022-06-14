"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tr1 = headA
        tr2 = headB
        intersect = 0
        intersect_value = 0
        while tr1 is not None:
            setattr(tr1, 'flag', 1)
            tr1 = tr1.next

        while tr2 is not None:
            try:
                flag = getattr(tr2, 'flag')
            except AttributeError:
                flag = 0

            if flag:
                intersect = 1
                intersect_value = tr2.val
                break
            tr2 = tr2.next

        if intersect:
            return tr2
        else:
            return None


if __name__ == '__main__':
    L5 = ListNode()