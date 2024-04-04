/**

https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/



**/

package main

import "slices"

func findGCD(nums []int) int {

	var smallest = slices.Max(nums)

	var largest = slices.Min(nums)

	var gcd = 1

	for i := 1; i <= smallest; i++ {
		if smallest%i == 0 && largest%i == 0 {
			if i > gcd {
				gcd = i
			}
		}
	}
	return gcd
}
