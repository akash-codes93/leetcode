"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def find_length(self, head):
        """
        Function to find the total length of the linked list
        :param head:
        :return:
        """
        count = 0
        while head is not None:
            count += 1
            head = head.next

        return count

    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pass
        length = self.find_length(head)
        # print(length)
        middle = length // 2
        print("middle:", middle)
        tr = head
        prev = None
        count = 0

        while count != middle:
            prev = tr
            tr = tr.next
            count += 1

        if prev is not None:
            prev.next = tr.next
        return head

    def print_linked_list(self, head):
        while head is not None:
            print(head.val)
            head = head.next


# l1 = ListNode(1)
# l2 = ListNode(2, l1)
# l3 = ListNode(3, l2)
# l4 = ListNode(4, l3)
# l5 = ListNode(5, l4)
l6 = ListNode(6)

Solution().print_linked_list(l6)
print("#######################")
a = Solution().deleteMiddle(l6)
print("#######################")
Solution().print_linked_list(l6)

