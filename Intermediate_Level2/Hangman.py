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
    """
]

# Ask user how many words they want to enter
num_words = int(input("How many words do you want to enter for the game? "))

# List to store words
words = []

for i in range(num_words):
    word = input(f"Enter word {i + 1}: ").lower()

    while not word.isalpha():
        word = input("Invalid input. Enter letters only: ").lower()

    words.append(word)

#Choosing random word
secret_word = random.choice(words)

# Hide secret word from guessing player
print("\n" * 50)

print("🎮 Welcome to Hangman!")
print("Hint: Guess the word entered by the user")

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