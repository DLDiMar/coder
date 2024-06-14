package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// Get the word from the first user
	fmt.Println("User 1, enter a word (no whitespace):")
	reader := bufio.NewReader(os.Stdin)
	word, _ := reader.ReadString('\n')
	word = strings.TrimSpace(word)
	if strings.Contains(word, " ") {
		fmt.Println("No whitespace allowed, please re-enter the word:")
		main()
		return
	}

	// Initialize the game
	guesses := 7
	for guesses > 0 {
		// Get the guess from the second user
		fmt.Printf("User 2, you have %d guesses left. Enter your guess:\n", guesses)
		guess, _ := reader.ReadString('\n')
		guess = strings.TrimSpace(guess)

		// Check the guess
		if guess == word {
			fmt.Println("Congratulations, you guessed the word!")
			return
		}

		// Print the colored output
		for i := 0; i < len(guess); i++ {
			if i >= len(word) {
				fmt.Print("\033[31m", string(guess[i]), "\033[0m") // red
			} else if guess[i] == word[i] {
				fmt.Print("\033[32m", string(guess[i]), "\033[0m") // green
			} else if strings.Contains(word, string(guess[i])) {
				fmt.Print("\033[33m", string(guess[i]), "\033[0m") // yellow
			} else {
				fmt.Print("\033[31m", string(guess[i]), "\033[0m") // red
			}
		}
		fmt.Println()

		guesses--
	}

	fmt.Println("Game over, the word was:", word)
}
