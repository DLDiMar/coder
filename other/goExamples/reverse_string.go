package main

import (
	"fmt"
	"strings"
)

func reverseString(s string) string {
	if len(s) == 0 {
		return ""
	}

	var builder strings.Builder

	for i := len(s) - 1; i >= 0; i-- {
		builder.WriteByte(s[i])
	}

	return builder.String()
}

func main() {
	fmt.Printf("Reverse of 'yes' is: %s", reverseString("yes"))
}
