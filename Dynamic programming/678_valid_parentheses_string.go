/**
https://leetcode.com/problems/valid-parenthesis-string/description/
**/

package main

import (
	"fmt"
)

func checkValidString(s string) bool {

	mem := map[[2]int]bool{}

	var dfs func(left int, i int) bool
	dfs = func(left int, i int) bool {
		// fmt.Println(val, isValid(val))
		if left < 0 {
			return false
		}

		if i >= len(s) {
			return left == 0
		}
		if data, ok := mem[[2]int{left, i}]; ok {
			// fmt.Println(val, ok)
			return data
		}

		var ans bool
		if string(s[i]) == "*" {
			ans = dfs(left+1, i+1) || dfs(left-1, i+1) || dfs(left, i+1)
		} else if string(s[i]) == "(" {
			ans = dfs(left+1, i+1)
		} else {
			ans = dfs(left-1, i+1)
		}
		// saving state
		mem[[2]int{left, i}] = ans
		return ans
	}
	return dfs(0, 0)
}

func main() {
	// ans := checkValidString("(*))")
	// ans := checkValidString("*(")
	// ans := checkValidString("(((((()*)(*)*))())())(()())())))((**)))))(()())()")
	ans := checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())")
	fmt.Println(ans)
}
