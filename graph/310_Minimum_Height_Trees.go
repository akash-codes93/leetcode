/*
*
https://leetcode.com/problems/minimum-height-trees/description/?envType=daily-question&envId=2024-04-23

can be soved using kahn's algorithm
or diameter	of tree

*
*/
package main

import "math"

func findMaxK(nums []int) int {

	mapNums := map[int]bool{}

	for _, num := range nums {
		mapNums[num] = true
	}

	for i := 1000; i >= -1000; i-- {

		_, pos := mapNums[i]

		_, neg := mapNums[-1*i]

		if pos && neg {
			return i
		}

	}

	return 0
}

func angleClock(hour int, minutes int) float64 {
	// find smallest angle from 12
	// the add both angle then ans is sum_angle or 360-sum_angle

	hour_angle := float64(hour*30) + float64(minutes)*0.5
	min_angle := float64(minutes * 6)

	angle := math.Abs(min_angle + hour_angle)

	if angle > 180 {
		angle = 360 - angle
	}
	return angle
}
