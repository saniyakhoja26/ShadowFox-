"""
Task Level: Advanced
Internship: ShadowFox Python Development
Name: Saniya Khoja
Project: Advanced Hangman Game
"""

import random

def get_words():
    num = int(input("How many words do you want to enter? "))
    words = []

    for i in range(num):
        word = input(f"Enter word {i + 1}: ").strip().lower()
        while not word.isalpha():
            word = input("Invalid input. Enter letters only: ").strip().lower()
        words.append(word)

    return words

def choose_difficulty():
    print("\nChoose Difficulty Level:")
    print("1. Easy (8 attempts)")
    print("2. Medium (6 attempts)")
    print("3. Hard (4 attempts)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 8
    elif choice == "2":
        return 6
    else:
        return 4

def get_hangman_stages():
    return [
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

def display_progress(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def save_score(player_name, score):
    with open("scores.txt", "a") as file:
        file.write(f"{player_name} : {score}\n")

def play_game():
    player = input("Enter player name: ")

    words = get_words()
    secret_word = random.choice(words)

    attempts = choose_difficulty()
    stages = get_hangman_stages()

    guessed_letters = []
    wrong_guesses = 0

    print("\n🎮 Game Started!")
    print("\n" * 30)  # hide secret word

    while True:
        print(stages[wrong_guesses])

        progress = display_progress(secret_word, guessed_letters)
        print("Word:", progress)
        print("Guessed letters:", guessed_letters)
        print("Attempts left:", attempts - wrong_guesses)

        if "_" not in progress:
            print("\n🎉 You WON!")
            save_score(player, 10)
            break

        guess = input("Guess a letter: ").strip().lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ Letter already guessed.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            wrong_guesses += 1
            print("❌ Wrong guess!")

        if wrong_guesses >= attempts:
            print(stages[-1])
            print("\n💀 Game Over!")
            print("The word was:", secret_word)
            save_score(player, 0)
            break

while True:
    play_game()
    replay = input("\nDo you want to play again? (y/n): ").lower()
    if replay != "y":
        print("Thanks for playing Advanced Hangman! 👋")
        break
