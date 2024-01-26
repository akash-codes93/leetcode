package main

import "fmt"

var mem = map[[2]int]int{}

func dfs(n int, state int) int {

	if n < 0 {
		return 0
	}

	if n == 0 {
		if state == 0 {
			return 1
		} else {
			return 0
		}
	}

	arr := [2]int{n, state}
	val, ok := mem[arr]
	if ok {
		return val
	}

	count := 0
	if state == 0 {
		if n >= 3 {
			count = (count + 2*dfs(n-2, 1)) % 1000000007
		}

		if n >= 1 {
			count = (count + dfs(n-1, 0) + dfs(n-2, 0)) % 1000000007
		}
	} else {
		count = (count + dfs(n-1, 1) + dfs(n-1, 0)) % 1000000007
	}

	mem[arr] = count
	return count

}

func numTilings(n int) int {
	return dfs(n, 0)
}

func main() {
	fmt.Println(numTilings(4))
}
