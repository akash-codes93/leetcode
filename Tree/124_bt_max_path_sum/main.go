package main

import (
	"fmt"
	"math"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getMax(arr ...int) int {
	max := arr[0]

	for i := range arr {
		if arr[i] > max {
			max = arr[i]
		}
	}
	return max
}

const MinVal = -10000000 * 3

func dfs(root *TreeNode, max []int) int {

	fmt.Println("entry ", max)

	if root == nil {
		return MinVal
	}

	left := dfs(root.Left, max)
	right := dfs(root.Right, max)

	max[0] = getMax(left, right, max[0], left+root.Val+right)
	fmt.Println("after ", max)

	return getMax(left+root.Val, right+root.Val, root.Val)

}

func maxPathSum(root *TreeNode) int {

	var max = []int{MinVal}
	out := dfs(root, max)
	return getMax(max[0], out)

}

func main() {

	var max = math.Inf(-1)

	var n = -3

	// if max > n {
	// 	fmt.Println(true)
	// } else {
	// 	fmt.Println(false)
	// }
	// fmt.Println(max > n)

}
