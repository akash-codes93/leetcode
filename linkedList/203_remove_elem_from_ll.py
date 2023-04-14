"""
https://leetcode.com/problems/remove-linked-list-elements/submissions/931977158/
"""


class Solution:
    def removeElements(self, head, val: int):
        prev = None
        tr = head

        while tr != None:

            if tr.val == val:
                if prev != None:
                    prev.next = tr.next
                else:
                    head = tr.next
            else:
                prev = tr

            tr = tr.next

        return head
