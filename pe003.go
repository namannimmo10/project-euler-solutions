package main

import "fmt"

func LargestPrimeFactor(num int) int {
	j := 2

	for (num % j) != 0 {
		j += 1
	}

	if (num % 2) == 0 {
		if num == 2 {
			return 2
		} else {
			return LargestPrimeFactor(num / 2)
		}
	} else if num/j == 1 {
		return num
	} else {
		return LargestPrimeFactor(num / j)
	}
}

func main() {
   fmt.Println(LargestPrimeFactor(600851475143)) // 6857
}
