import random

words = ["apple", "python", "mango", "school", "computer"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You Win!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if wrong_guesses == max_guesses:
    print("Game Over! The word was:", secret_word)