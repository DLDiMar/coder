package main

import "fmt"

func SumTwo(x int, y int) int {
	return x + y
}

func main() {
	fmt.Printf("First sum: %d\n", SumTwo(2, 3))
	fmt.Printf("Last sum: %d\n", SumTwo(3, 4))
}
