package main

import "fmt"

func sumArray(arr []int) int {
	sum := 0

	for i := 0; i < len(arr); i++ {
		sum += arr[i]
	}

	return sum
}

func main() {
	fmt.Printf(" Total for array: %d", sumArray([]int{1, 2, 3, 4}))
}
