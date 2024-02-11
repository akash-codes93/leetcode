package main

func leastBricks(wall [][]int) int {
	gap := map[int]int{}
	sumEachRow := 0

	for i, _ := range wall {
		sum := 0
		for j, _ := range wall[i] {
			sum += wall[i][j]
			_, ok := gap[sum]
			if ok {
				gap[sum] += 1
			} else {
				gap[sum] = 1
			}
		}
		if sumEachRow == 0 {
			sumEachRow = sum
		}
	}

	// removing last idx as it will always be true
	delete(gap, sumEachRow)
	// fmt.Println(gap)

	maxValue := 0
	for _, value := range gap {
		if value > maxValue {
			maxValue = value
		}
	}
	return len(wall) - maxValue

}
