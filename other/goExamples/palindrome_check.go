package main

import "fmt"

func IsPalindrome(s string) bool {
	for i := 0; i < len(s)/2; i++ {
		if s[i] != s[len(s)-1-i] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Printf("Is racecar a palindrome? %t\n", IsPalindrome("racecar"))
	fmt.Printf("Is car a palindrome? %t\n", IsPalindrome("car"))
}
