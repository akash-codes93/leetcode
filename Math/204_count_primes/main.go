package main

import "fmt"

func seieveOfErathoneses(n int, isPrime []bool) {

	isPrime[0] = false
	isPrime[1] = false

	for p := 2; p*p <= n; p++ {

		if isPrime[p] == true {
			for i := p * p; i <= n; i = i + p {
				isPrime[i] = false

			}
		}

	}
}

func primesum(A int) []int {

	isPrime := make([]bool, A+1)
	for j := range isPrime {
		isPrime[j] = true
	}

	seieveOfErathoneses(A, isPrime)
	fmt.Println(isPrime)
	for i := 0; i <= A; i++ {
		if isPrime[i] == true && isPrime[A-i] == true {
			arr := []int{i, A - i}
			return arr
		}
	}
	return []int{}
}

func main() {
	fmt.Println(primesum(4))
}
