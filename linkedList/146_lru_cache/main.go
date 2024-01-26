package main

import "fmt"

type Node struct {
	val  int
	key  int
	next *Node
	prev *Node
}

type LinkedList struct {
	start *Node
	end   *Node
}

func NewLinkedList() LinkedList {
	start := Node{
		0,
		0,
		nil,
		nil,
	}

	end := Node{
		0,
		0,
		nil,
		nil,
	}

	start.next = &end
	end.prev = &start

	ll := LinkedList{
		start: &start,
		end:   &end,
	}

	return ll

}

func (ll *LinkedList) remove(node *Node) {

	prev := node.prev
	next := node.next

	prev.next = next
	next.prev = prev

}

func (ll *LinkedList) insert(node *Node) {
	next := ll.end
	prev := ll.end.prev
	fmt.Println(next, prev)

	//node
	node.next = next
	node.prev = prev

	// next
	next.prev = node

	// prev
	prev.next = node

}

type LRUCache struct {
	capacity int
	ll       *LinkedList
	nodeMap  map[int]*Node
}

func Constructor(capacity int) LRUCache {
	m := map[int]*Node{}
	ll := NewLinkedList()
	lruCache := LRUCache{
		capacity,
		&ll,
		m,
	}

	return lruCache
}

func (this *LRUCache) Get(key int) int {
	node, ok := this.nodeMap[key]

	if ok == false {
		return -1
	}

	this.ll.remove(node)
	this.ll.insert(node)

	return node.val

}

func (this *LRUCache) Put(key int, value int) {
	node, ok := this.nodeMap[key]

	if ok {
		node.val = value
		this.ll.remove(node)
		this.ll.insert(node)

	} else {
		if len(this.nodeMap) == this.capacity {
			oldNode := this.ll.start.next
			delete(this.nodeMap, oldNode.key)
			this.ll.remove(oldNode)
		}

		newNode := &Node{
			value,
			key,
			nil,
			nil,
		}
		this.ll.insert(newNode)
		this.nodeMap[key] = newNode
	}

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
