# Project 1: Quiz Game
# Goal: Create a quiz game where users are asked questions until they choose to quit.
#
# Requirements:
# Create a list of 20 questions and their answers.
# Use a while loop to ask the questions one by one.
# Use a function check_answer(question, answer) to verify the user's input.
# Keep a score of correct answers.
# Allow the user to quit at any time by typing "quit".

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest mammal?", "Blue whale"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the smallest country in the world?", "Vatican"),
    ("What is the largest ocean on Earth?", "Pacific"),
    ("What is the most common gas in the Earth's atmosphere?", "Nitrogen"),
    ("What is the largest continent?", "Asia"),
    ("What is the tallest mountain in the world?", "Everest"),
    ("What is the smallest planet in our solar system?", "Mercury"),
    ("What is the most common element in the Earth's crust?", "Oxygen"),
    ("What is the most common element in the universe?", "Hydrogen"),
    ("What is the largest desert in the world?", "antarctica"),
    ("What is the largest bird in the world?", "ostrich"),
    ("What is the largest country in the world?", "russia"),
    ("What is the largest lake in the world?", "caspian sea"),
    ("What is the smallest ocean on Earth?", "arctic"),
    ("What is the smallest continent?", "australia"),
    ("What is the smallest country in Africa?", "seychelles"),
    ("What is the largest river in the world?", "amazon"),
    ("What is the largest island in the world?", "greenland")
]

score = 0
total_questions = len(questions)
asked_questions = 0

while True:
    for question, answer in questions:
        user_answer = input(question + " ")
        if user_answer.lower() == "quit":
            break

        asked_questions += 1

        if user_answer.lower() == answer:
            score += 1
            print("Correct!")
        else:
            print("Incorrect!")
            print("The correct answer is:", answer)

        if asked_questions == total_questions:
            print("All questions have been asked!")
            print("Your final score is:", score)
            break
    else:
        continue
    break

