package main

import "fmt"

type Node struct {
	val  int
	next *Node
	prev *Node
}

type MyLinkedList struct {
	start *Node
	end   *Node
	cap   int
}

func Constructor() MyLinkedList {
	start := Node{
		val:  0,
		next: nil,
		prev: nil,
	}

	end := Node{
		val:  0,
		next: nil,
		prev: nil,
	}

	start.next = &end
	end.prev = &start

	var linkedList = MyLinkedList{
		start: &start,
		end:   &end,
		cap:   0,
	}

	return linkedList
}

func (this *MyLinkedList) GetNodeAtIndex(index int) *Node {
	tr := this.start
	st := -1

	for st != index {
		tr = tr.next
		st += 1
	}

	return tr
}

func (this *MyLinkedList) InsertNextTo(node *Node, val int) {
	newNode := Node{
		val: val,
	}

	temp := node.next

	newNode.next = temp
	newNode.prev = node

	node.next = &newNode
	temp.prev = &newNode

}

func (this *MyLinkedList) Get(index int) int {

	if index >= this.cap {
		return -1
	}
	node := this.GetNodeAtIndex(index)
	return node.val

}

func (this *MyLinkedList) AddAtHead(val int) {

	this.cap += 1
	// after start node
	this.InsertNextTo(this.start, val)
}

func (this *MyLinkedList) AddAtTail(val int) {
	this.cap += 1
	// one node before end node
	this.InsertNextTo(this.end.prev, val)
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index > this.cap {
		return
	}
	node := this.GetNodeAtIndex(index - 1)
	this.InsertNextTo(node, val)
	this.cap += 1
}

func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index >= this.cap {
		return
	}
	node := this.GetNodeAtIndex(index)
	prev := node.prev
	next := node.next

	prev.next = next
	next.prev = prev
	this.cap -= 1

}

func (this *MyLinkedList) Print() {
	tr := this.start

	for tr != this.end {

		fmt.Print(tr.val)
		tr = tr.next
	}
}

func main() {
	ll := Constructor()
	ll.AddAtHead(1)
	ll.AddAtTail(3)
	ll.AddAtIndex(1, 2)
	ll.Print()
	fmt.Println()

}
