package main

import (
	"errors"
	"fmt"
)

func findDuplicate(arr []int) (int, error) {
	// Create a map to keep track of seen values
	alreadyFound := make(map[int]bool)

	// Loop through the array
	for _, value := range arr {
		// If current value is already seen, return the value and no error
		if alreadyFound[value] {
			return value, nil
		}
		// Mark the current value as seen
		alreadyFound[value] = true
	}

	// If no duplicate is found, return 0 and an error
	return 0, errors.New("no duplicate found in the array")
}

func main() {
	testCases := [][]int{
		{1, 1, 2, 4, 5},
		{1, 3, 2, 4, 5},
		{-1, 3, -1, 4, 5},
	}

	for _, testCase := range testCases {
		if value, err := findDuplicate(testCase); err == nil {
			fmt.Printf("The duplicate in the array: %d\n", value)
		} else {
			fmt.Println(err)
		}
	}
}
