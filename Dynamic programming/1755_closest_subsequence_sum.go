package main

import (
	"math"
	"sort"
)

// not DP as thought

func minAbsDifference(nums []int, goal int) int {

	mid := len(nums) / 2
	ans := math.MaxInt

	var first_half = nums[:mid]
	var second_half = nums[mid:]
	subsets_sum1 := GetAllSubsetSum(first_half)
	subsets_sum2 := GetAllSubsetSum(second_half)

	sort.Slice(subsets_sum2, func(i, j int) bool {
		return subsets_sum2[i] < subsets_sum2[j]
	})
	for i := 0; i < len(subsets_sum1); i++ {
		req_sum := goal - subsets_sum1[i]

		idx := sort.Search(len(subsets_sum2), func(j int) bool { return subsets_sum2[j] >= req_sum })
		// checking the boundaries
		if idx > 0 {
			ans = int(math.Min(float64(ans), math.Abs(float64(goal-subsets_sum2[idx-1]-subsets_sum1[i]))))
		}
		if idx < len(subsets_sum2) {
			ans = int(math.Min(float64(ans), math.Abs(float64(goal-subsets_sum2[idx]-subsets_sum1[i]))))
		}
	}
	return ans
}

func GetAllSubsetSum(nums []int) []int {
	sum := []int{}

	var dfs func(i, s int)
	dfs = func(i, s int) {
		if i == len(nums) {
			sum = append(sum, s)
			return
		}
		for choice := 0; choice < 2; choice++ {
			// not include
			if choice == 0 {
				dfs(i+1, s)
			} else {
				//include
				dfs(i+1, s+nums[i])
			}
		}
	}
	dfs(0, 0)
	return sum
}

func main() {
	minAbsDifference([]int{5, -7, 3, 5}, 6)
	minAbsDifference([]int{7, -9, 15, -2}, -5)
	minAbsDifference([]int{1, 2, 3}, -7)
	// a := []int{0, 1, 1, 1, 2, 3, 3, 5}
	// idx := sort.Search(len(a), func(i int) bool { return a[i] >= 6 })
	// fmt.Println(idx)
	// a := 1
	// b := 2
	// fmt.Println(math.Abs(a))
}
