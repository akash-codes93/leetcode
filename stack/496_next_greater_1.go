package main

import (
	"fmt"
	"slices"
)

// pre condiditon all elems in nums2 are unique

type Stack []int

func (s Stack) Push(x int) Stack {
	return append(s, x)
}

func (s Stack) Pop() (Stack, int) {
	elem := s[len(s)-1]
	s = s[:len(s)-1]
	return s, elem
}

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	elemMap := make(map[int]int)
	stack := make(Stack, 0)

	slices.Reverse(nums2)

	for _, i := range nums2 {

		for len(stack) > 0 && stack[len(stack)-1] < i {
			stack, _ = stack.Pop()
		}

		if len(stack) > 0 {
			elemMap[i] = stack[len(stack)-1]
		} else {
			elemMap[i] = -1
		}
		stack = stack.Push(i)
		// fmt.Println(stack)
	}
	// fmt.Println(elemMap)
	output := []int{}

	for _, i := range nums1 {
		output = append(output, elemMap[i])
	}

	return output
}

func main() {
	o := nextGreaterElement([]int{4, 1, 2}, []int{1, 3, 4, 2})

	fmt.Println(o)
}
