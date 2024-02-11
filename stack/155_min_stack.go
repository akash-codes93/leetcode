package main

import "math"

type MinStack struct {
	stack   []int
	minElem int
}

func Constructor() MinStack {
	minStack := MinStack{
		stack:   make([]int, 0),
		minElem: math.MaxInt,
	}

	return minStack
}

func (this *MinStack) Push(val int) {
	// zero case should be handled separately
	if len(this.stack) == 0 {
		this.stack = append(this.stack, val)
		this.minElem = val
	} else {
		if val > this.minElem {
			this.stack = append(this.stack, val)
		} else {
			this.stack = append(this.stack, 2*val-this.minElem)
			this.minElem = val
		}
	}
}

func (this *MinStack) Pop() {
	top_elem := this.stack[len(this.stack)-1]
	if top_elem < this.minElem {
		this.minElem = 2*this.minElem - top_elem
	}

	this.stack = this.stack[:len(this.stack)-1]

}

func (this *MinStack) Top() int {
	top_elem := this.stack[len(this.stack)-1]
	elem := top_elem
	if top_elem < this.minElem {
		elem = this.minElem
	}

	return elem
}

func (this *MinStack) GetMin() int {
	return this.minElem
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
