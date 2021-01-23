package main

import "fmt"

const MAX = 4000000

// Prints the sum of even-valued fibonacci terms under 4 million
func SumEvenFibonacci() int {
	a := 1
	b := 2
	sum := 2
	next := a + b

	for next < MAX {
		if (next & 1) == 0 {
			sum += next
		}
		a = b
		b = next
		next = a + b
	}

	return sum
}

func ExampleSumEvenFibonacci() {
    fmt.Println(SumEvenFibonacci())
    // Output: 4613732
}

func main() {
	fmt.Println("The sum of even-valued fibonacci terms under 4 million is: ", SumEvenFibonacci())
}
