package main

import "fmt"

type Node struct {
	endsHere  bool
	value     byte
	score     int
	nextChars [26]*Node
}

type Trie struct {
	baseNode *Node
}

func newNode(endsHere bool, value byte, score int) *Node {
	var nextChars [26]*Node

	for i := range nextChars {
		nextChars[i] = nil
	}

	return &Node{
		endsHere:  endsHere,
		value:     value,
		score:     score,
		nextChars: nextChars,
	}
}

func (tr *Trie) insert(word string, score int) {
	i := 0
	t := tr.baseNode

	for i < len(word) {
		var node *Node
		idx := word[i] - 97
		if t.nextChars[idx] == nil {
			node = newNode(false, word[i], 0)
			t.nextChars[idx] = node
		} else {
			node = t.nextChars[idx]
		}

		if i == len(word)-1 {
			node.endsHere = true
			node.score = score
		}

		t = node
		i += 1
	}
}

func sumAll(node *Node) int {
	score := 0

	if node.endsHere {
		score += node.score
	}

	for i := 0; i < 26; i++ {
		if node.nextChars[i] != nil {
			score += sumAll(node.nextChars[i])
		}
	}
	return score
}

func (tr *Trie) sum(word string) int {
	var score int = 0
	i := 0
	t := tr.baseNode

	for i < len(word) {
		var node *Node
		idx := word[i] - 97
		if t.nextChars[idx] == nil {
			return score
		} else {
			node = t.nextChars[idx]
		}
		t = node
		i += 1
	}
	return sumAll(t)
}

type MapSum struct {
	trie *Trie
}

func Constructor() MapSum {
	var nextChars [26]*Node

	for i := range nextChars {
		nextChars[i] = nil
	}

	baseNode := Node{
		endsHere:  false,
		value:     '/',
		score:     0,
		nextChars: nextChars,
	}

	trie := Trie{
		baseNode: &baseNode,
	}

	mapSum := MapSum{
		trie: &trie,
	}
	return mapSum
}

func (this *MapSum) Insert(key string, val int) {
	this.trie.insert(key, val)
}

func (this *MapSum) Sum(prefix string) int {
	return this.trie.sum(prefix)
}

func main() {
	// Your MapSum object will be instantiated and called as such:

	obj := Constructor()
	obj.Insert("apple", 3)
	param_2 := obj.Sum("ap")

	obj.Insert("app", 3)
	param_2 = obj.Sum("ap")
	fmt.Println(param_2)

}
