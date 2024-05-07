package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	lenA := 0
	lenB := 0

	trA := headA
	trB := headB
	//find length of both linked list
	for trA.Next != nil {
		trA = trA.Next
		lenA++
	}

	for trB.Next != nil {
		trB = trB.Next
		lenB++
	}
	lenA = lenA + 1
	lenB = lenB + 1
	// fmt.Println(lenA, lenB)

	// if tail is different no intersection
	if trA != trB {
		return nil
	}
	// if same len create new heads
	trA = &ListNode{
		Val:  0,
		Next: headA,
	}
	trB = &ListNode{
		Val:  0,
		Next: headB,
	}
	// moving the longer
	if lenA > lenB {

		for i := 0; i < lenA-lenB; i++ {
			trA = trA.Next
		}
	} else if lenA < lenB {
		for i := 0; i < lenB-lenA; i++ {
			trB = trB.Next
		}
	}
	// finding the intersection node
	for trA != nil && trB != nil && trA.Next != trB.Next {
		trA = trA.Next
		trB = trB.Next
	}
	return trA.Next
}
