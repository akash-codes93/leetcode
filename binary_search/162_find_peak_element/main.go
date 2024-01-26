package main

import (
	"fmt"
	"math"
)

func findPeakElement(nums []int) int {

	l, r := 0, len(nums)-1

	var (
		val   int
		left  int
		right int
		mid   int
	)

	for l <= r {
		mid = (r - (r-l)/2)
		val = nums[mid]
		left = math.MinInt
		right = math.MinInt

		if mid-1 >= 0 {
			left = nums[mid-1]
		}

		if mid+1 < len(nums) {
			right = nums[mid+1]
		}

		fmt.Println(mid, left, val, right)

		if left < val && val > right {
			return mid
		} else if left < val && val < right {
			l = mid + 1
		} else if left > val && val > right {
			r = mid - 1
		} else {
			l = mid + 1
		}

	}

	return mid

}

func main() {
	fmt.Println(math.MinInt)
	arr := []int{2, 1}
	fmt.Println(findPeakElement(arr))
}
