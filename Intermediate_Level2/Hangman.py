"""
Task Level: Intermediate
Internship: ShadowFox Python Development
Name: Saniya Khoja
Task: Hangman Game (Classic Version)
"""

import random

hangman_stages = [
    """
      -----
      |   |
          |
          |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    ---------
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ---------
    """,
]

# Predefine a list of words
words_list = [
    "python",
    "development",
    "hangman",
    "shadowfox",
    "programming",
    "challenge",
    "function",
    "variable",
]
while True:
    # Choosing random word
    secret_word = random.choice(words_list)

    print("🎮 Welcome to Hangman!")
    print("Hint: Guess the word")

    guessed_letters = []
    wrong_guesses = 0
    max_wrong = len(hangman_stages) - 1

    # Game loop
    while True:
        # Display hangman stage
        print(hangman_stages[wrong_guesses])

        # Display word progress
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word.strip())
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", max_wrong - wrong_guesses)

        # Check win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly.")
            break

        # Take user guess
        guess = input("Guess a letter: ").lower()

        # Validation
        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Wrong guess
        if guess not in secret_word:
            wrong_guesses += 1
            print("❌ Wrong guess!")

        # Lose condition
        if wrong_guesses == max_wrong:
            print(hangman_stages[wrong_guesses])
            print("\n💀 Game Over!")
            print("The word was:", secret_word)
            break

    # Play Again Option
    play_again = input("Do you want to play again? (yes/y or no/n): ").lower()
    if play_again != "yes" and play_again != "y":
        print("Thank you for playing Hangman! Goodbye!")
        break
