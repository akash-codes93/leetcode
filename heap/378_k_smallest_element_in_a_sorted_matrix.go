/**

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

Idea: store first row in the min heap

pop elements from the heap and push next element (row) into the heap
do this k times

**/

package main

import (
	"fmt"
)

type Element struct {
	val int
	i   int
	j   int
}

func min_heapify(arr *[]Element, i int, heap_size int) {
	left := 2*i + 1
	right := 2*i + 2

	var smallest int
	smallest = i

	if left < heap_size && (*arr)[left].val < (*arr)[smallest].val {
		smallest = left
	}

	if right < heap_size && (*arr)[right].val < (*arr)[smallest].val {
		smallest = right
	}

	if i != smallest {
		(*arr)[i], (*arr)[smallest] = (*arr)[smallest], (*arr)[i]
		min_heapify(arr, smallest, heap_size)
	}
}

func min_perculate_up(arr *[]Element, elem Element) {
	*arr = append(*arr, elem)
	i := len(*arr) - 1

	for i > 0 {
		parent := (i - 1) / 2
		// fmt.Println("parent", parent)
		if (*arr)[parent].val < (*arr)[i].val {
			break
		}
		(*arr)[parent], (*arr)[i] = (*arr)[i], (*arr)[parent]
		i = parent
	}
}

func kthSmallest(matrix [][]int, k int) int {

	heap := []Element{}
	for i := 0; i < len(matrix); i++ {
		elem := Element{
			val: matrix[i][0],
			i:   i,
			j:   0,
		}
		min_perculate_up(&heap, elem)
		// fmt.Println(heap)
	}
	// fmt.Println(heap)
	for k > 1 {
		val := heap[0]
		if val.j < len(matrix)-1 {
			heap[0] = Element{
				val: matrix[val.i][val.j+1],
				i:   val.i,
				j:   val.j + 1,
			}
		} else {
			heap[0] = heap[len(heap)-1]
			heap = heap[:len(heap)-1]
		}
		min_heapify(&heap, 0, len(heap))
		// fmt.Println(heap)
		k--
	}
	return heap[0].val
}

func main() {
	matrix := [][]int{{1, 5, 9}, {10, 11, 13}, {12, 13, 15}}
	// matrix := [][]int{{-5}}
	k := 8
	fmt.Println(kthSmallest(matrix, k))
}
