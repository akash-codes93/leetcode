/**
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/

without reversing the ll using the fact that node will only create a carry if node.Val > 4

**/

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func doubleIt(head *ListNode) *ListNode {
	curr := head

	if curr.Val > 4 {
		head = &ListNode{Val: 1, Next: head}
	}

	for curr.Next != nil {
		curr.Val = curr.Val * 2
		if curr.Next.Val > 4 {
			curr.Val += 1
		}
		curr.Val = (curr.Val) % 10
		curr = curr.Next
	}
	curr.Val = (curr.Val * 2) % 10
	return head
}
