/*
*
https://leetcode.com/problems/remove-nodes-from-linked-list/

*
*/
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverse(head *ListNode) *ListNode {
	var prev *ListNode
	prev = nil

	tr := head

	for tr != nil {
		next := tr.Next
		tr.Next = prev

		prev = tr
		tr = next
	}

	return prev
}

func removeNodes(head *ListNode) *ListNode {
	newHead := reverse(head)
	tr := newHead.Next
	prev := newHead

	for tr != nil {
		if tr.Val < prev.Val {
			prev.Next = tr.Next
		} else {
			prev = tr
		}
		tr = tr.Next
	}
	head = reverse(newHead)
	return head

}
