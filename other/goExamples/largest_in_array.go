package main

import "fmt"

func largestInArray(arr []int) int {
	largest := arr[0]

	for i := 1; i < len(arr); i++ {
		if arr[i] > largest {
			largest = arr[i]
		}
	}
	return largest
}

func main() {
	fmt.Printf("Largest value in array: %d", largestInArray([]int{0}))
}
