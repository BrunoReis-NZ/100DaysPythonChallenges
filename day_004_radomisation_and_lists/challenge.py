import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

print("What do you choose? Type O for Rock, 1 for Paper or 2 for Scissors.\n")
players_choice = int(input())

if players_choice == 0:
    print(rock)
elif players_choice == 1:
    print(paper)
elif players_choice == 2:
    print(scissors)
else:
    print("Invalid. Game over")

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if players_choice == 0 and computer_choice == 1:
    print ("computer won")
elif players_choice == 0 and computer_choice == 2:
    print("player won")
elif players_choice == 1 and computer_choice == 0:
    print ("player won")
elif players_choice == 1 and computer_choice == 2:
    print("computer won")
elif players_choice == 2 and computer_choice == 0:
        print("computer won")
elif players_choice == 2 and computer_choice == 1:
        print("player won")
else:
    print("Its a draw")