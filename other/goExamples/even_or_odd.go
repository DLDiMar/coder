package main

import "fmt"

func EvenOrOdd(n int) string {
	if n%2 == 0 {
		return "even"
	} else {
		return "odd"
	}
}

func main() {
	fmt.Printf("Is 2 even or odd?: %s\n", EvenOrOdd(2))
	fmt.Printf("Is 1 even or odd?: %s\n", EvenOrOdd(1))
}
