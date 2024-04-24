/**
https://leetcode.com/problems/rotate-list/description/

idea is simple connect last node to first node to make it circular
and break it at a point

**/

package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil || k == 0 {
		return head // base case only one Node
	}

	len := 0
	tr := head
	var prev *ListNode

	for tr != nil {
		len += 1
		prev = tr
		tr = tr.Next
	}

	prev.Next = head
	k = k % len     // overshoot problem
	k = len - k - 1 // new k because of circular

	tr = head
	for k != 0 {
		tr = tr.Next
		k--
	}

	prev = tr    // tr is tail not
	tr = tr.Next // tr is the new head

	prev.Next = nil
	return tr
}
