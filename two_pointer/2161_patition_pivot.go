package main

import "fmt"

func pivotArray(nums []int, pivot int) []int {
	count_smaller := 0
	count_equal := 0

	for j := 0; j < len(nums); j++ {
		if nums[j] < pivot {
			count_smaller++
		} else if nums[j] == pivot {
			count_equal++
		}
	}

	smaller := 0
	equal := count_smaller
	greater := count_smaller + count_equal
	result := make([]int, len(nums))

	for j := 0; j < len(nums); j++ {
		if nums[j] < pivot {
			result[smaller] = nums[j]
			smaller++
		} else if nums[j] == pivot {
			result[equal] = nums[j]
			equal++
		} else {
			result[greater] = nums[j]
			greater++
		}
	}

	return result
}

func main() {
	res := pivotArray([]int{9, 12, 5, 10, 14, 3, 10}, 10)
	fmt.Println(res)
}
