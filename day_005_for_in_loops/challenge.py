import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!\n")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))


# Easy version

password_EV = ""

for letter in range (nr_letters):
    password_EV += random.choice(letters)
for symbol in range (nr_symbols):
    password_EV += random.choice(symbols)
for number in range(nr_numbers):
    password_EV += random.choice(numbers)

print(f"Your secure easy version password is {password_EV}")

# Hard version

password_as_list = []

for letter in range (nr_letters):
    password_as_list.append(random.choice(letters))
for symbol in range (nr_symbols):
    password_as_list.append(random.choice(symbols))
for number in range(nr_numbers):
    password_as_list.append(random.choice(numbers))

random.shuffle(password_as_list)
password_HV = "".join(password_as_list)

print(f"Your secure hard version password is {password_HV}")