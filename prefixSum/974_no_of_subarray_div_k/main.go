package main

import "fmt"

func subarraysDivByK(nums []int, k int) int {
	freq := map[int]int{
		0: 1,
	}
	sum := 0
	var rem int
	count := 0

	for _, i := range nums {
		fmt.Println(i)
		sum += i
		rem = sum % k

		if val, ok := freq[rem]; ok {
			count += val
			freq[rem] += 1
		} else {
			freq[rem] = 1
		}
	}
	return count
}

func main() {
	fmt.Println(subarraysDivByK([]int{4, 5, 0, -2, -3, 1}, 5))
}
