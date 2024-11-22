# Project 2: Number Guessing Game
# Goal: Create a number guessing game with difficulty levels.
#
# Requirements:
# Use a function generate_number(difficulty) to generate a random number based on the difficulty:
# Easy: 1-10
# Medium: 1-50
# Hard: 1-100
# Allow the user to guess the number until they get it right or type "quit".
# Count the number of attempts and display it at the end.

import random

def generate_number(difficulty):
    if difficulty.lower() == "easy" or difficulty.lower() == "e":
       return random.randint(1, 10)
    if difficulty.lower() == "medium" or difficulty.lower() == "m":
       return random.randint(1, 50)
    if difficulty.lower() == "hard" or difficulty.lower() == "h":
        return random.randint(1, 100)
    else:
        return "Wrong difficult level!"

difficult_level = input("Choose a difficult level (Easy, Medium, Hard): ")
target = generate_number(difficult_level)
attempts = 1

while True:

    if difficult_level.lower() == "easy" or difficult_level.lower() == "e":
        guess = input("guess a number between 1 and 10: ")
    elif difficult_level.lower() == "medium" or difficult_level.lower() == "m":
        guess = input("guess a number between 1 and 50: ")
    else:
        guess = input("guess a number between 1 and 100: ")

    if guess.lower() == "quit" or guess.lower() == "q":
        print("See you soon!")
        break

    if int(guess) == target:
        print("Congratulations! You guessed right!")
        break
    elif int(guess) > target:
        print("You guessed too high")
        print("Try again: ")
    else:
        print("You guessed too low")
        print("Try again: ")

    attempts += 1

print(f"\nNumber of attempts: {attempts}")
