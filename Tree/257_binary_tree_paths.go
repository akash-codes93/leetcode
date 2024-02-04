package main

import (
	"strconv"
)

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func binaryTreePaths(root *TreeNode) []string {

	// var allPaths []string

	// function declaration synxtax
	var dfs func(node *TreeNode) []string

	dfs = func(root *TreeNode) []string {
		if root == nil {
			return []string{}
		}

		if root.Left == nil && root.Right == nil {
			return []string{strconv.Itoa(root.Val)}
		}

		leftPaths := []string{}
		if root.Left != nil {
			leftPaths = dfs(root.Left)
		}

		rightPaths := []string{}
		if root.Right != nil {
			rightPaths = dfs(root.Right)
		}

		allPaths := []string{}
		var newPath string = ""
		_ = newPath
		for _, path := range leftPaths {
			newPath = strconv.Itoa(root.Val) + "->" + path
			allPaths = append(allPaths, newPath)
		}

		for _, path := range rightPaths {
			newPath = strconv.Itoa(root.Val) + "->" + path
			allPaths = append(allPaths, newPath)
		}

		return allPaths

	}

	return dfs(root)

}
