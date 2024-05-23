/*
*
https://leetcode.com/problems/palindrome-partitioning/description/

*
*/
package main

import "fmt"

func isPalindrome(s string) bool {
	var reverseString string = ""
	var length = len(s)
	for i := length - 1; i >= 0; i-- {
		reverseString = reverseString + string(s[i])
	}
	return s == reverseString
}

func partition(s string) [][]string {

	mem := map[string][][]string{}

	var dfs func(s string) [][]string

	dfs = func(suffix string) [][]string {

		val, ok := mem[suffix]
		if ok {
			return val
		}

		if len(suffix) == 0 {
			return [][]string{[]string{}}
		} else if len(suffix) == 1 {
			return [][]string{[]string{suffix}}
		} else {
			result := [][]string{}

			for i := 1; i <= len(suffix); i++ {
				if isPalindrome(suffix[:i]) {
					right := dfs(suffix[i:])
					// fmt.Println(right)
					for _, r := range right {
						// fmt.Println(r)
						left := []string{suffix[:i]}
						left = append(left, r...)
						// fmt.Println("lwft", left)
						result = append(result, left)
					}
				}
			}
			mem[suffix] = result
			return result
		}
	}
	return dfs(s)
}

func main() {
	d := partition("aab")
	fmt.Println(d)
}
