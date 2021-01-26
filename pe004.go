package main

import "fmt"

func IsPalindrome(num int) bool {
	reversed, originalNum := 0, num

	for num > 0 {
		reversed = reversed*10 + num%10
		num /= 10
	}

	if originalNum == reversed {
		return true
	} else {
		return false
	}
}

func LargestPalindrome() int {
	result, a := 0, 999

	for a >= 100 {
		b := 999
		for b >= a {
			prod := a * b
			if IsPalindrome(prod) {
				if prod > result {
					result = prod
				}
			}
			b--
		}
		a--
	}

	return result
}

func main() {
   fmt.Println(LargestPalindrome()) // 906609
}
