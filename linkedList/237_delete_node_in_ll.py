"""
https://leetcode.com/problems/delete-node-in-a-linked-list/

very easy do in single pass

"""


class Solution:

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        tr = node
        while tr.next != None:

            tr.val = tr.next.val

            if tr.next.next == None:
                tr.next = None
            else:
                tr = tr.next
