class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return

        slow = head
        fast = head

        while fast is not None and fast.next != None:

            fast = fast.next
            slow = slow.next

            if fast != None:
                fast = fast.next

        if slow is None or slow.next is None:
            return
        print(slow.val)

        prev = None
        start = slow.next
        while start != None:
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        print("heare")
        slow.next = prev

        tr = head

        while tr != None:
            print(tr.val)
            tr = tr.next

        first = head

        second = slow.next
        slow.next = None

        while second:
            # print(second.val)
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        print("---")
        tr = head
        while tr != None:
            print(tr.val)
            tr = tr.next

        return


ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().reorderList(ll)

