import random

# # Functions in Python
#
# # 1
# print("\n1. Simple Function Definition and Call. \n"
#       "Define a function greet() that prints 'Hello, welcome to Python!'. \n"
#       "Call the function.\n")
#
# def greet():
#     print("Hello, Welcome to Python")
#
# greet()
#
# # 2
#
# print("\n2. Function with Parameters. \n"
#       "Define a function greet_name(name) that takes a name as a parameter \n"
#       "and prints 'Hello, [name]!'.")
#
# def greet_name(name):
#     print(f"Hello, {name}!")
#
# greet_name("Bruno")
#
# # 3
#
# print("\n3. Function with Return Value. \n"
#       "Write a function square(num) that returns the square of a number.")
#
# def square(num):
#     return num * num
#
# num = 2
# print(f"The square of {num} is {square(num)}")
#
# # 4
#
# print("\n4. Function with Multiple Parameters. \n"
#       "Write a function add_numbers(a, b) that takes two numbers as parameters and returns their sum.")
#
# def add_numbers(num1, num2):
#     return num1 + num2
#
# num1 = 4
# num2 = 5
#
# print(f"The sum of {num1} + {num2} is {add_numbers(num1, num2)}")
#
# # 5
#
# print("\n5. Default Parameter Value. \n"
#       "Define a function greet_user(name='User') that greets the user. \n"
#       "If no name is provided, it should use 'User'.")
#
# def greet_user(name="User"):
#     print(f"Kia Ora, {name}!")
#
# greet_user("Bruno")
# greet_user()
#
# # While Loops
#
# # 6
#
# print("\n6. Simple Countdown. \n"
#       "Write a while loop to print numbers from 10 to 1, then print 'Liftoff!'.")
#
# count = 10
# while count > 0:
#     print(count)
#     count -= 1
# print("Liftoff")
#
# # 7
#
# print("\n7. Simple User Input Loop. \n"
#       "Write a while loop that asks the user to input a number. \n"
#       "Exit the loop if the user enters a negative number.")
#
# while True:
#     num = int(input("Enter a number (negative to quit): "))
#     if num < 0:
#         break
#
# # 8
#
# print("\n8. Sum Until Zero. \n"
#       "Write a program that keeps asking the user for numbers and calculates their sum. \n"
#       "Stop when the user enters 0")
#
# total = 0
#
# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         break
#     total += num
#     print(f"The total is: {total}.")
#
# # 9
#
# print("\n9. Infinite Loop with Break. \n"
#       "Create an infinite loop that prints 'Processing...' but stops after printing it 5 times using a break.")
#
# count = 0
# while True:
#     print("Processing...")
#     count += 1
#     if count == 5:
#         break

# # 10
#
# print("\n10. Using continue. \n"
#       "Write a program that prints numbers from 1 to 10, but skips numbers divisible by 3 using continue.")
#
# count = 1
# while count <= 10:
#     if count % 3 == 0:
#         count += 1
#         continue
#     print(count)
#     count += 1

# # 11
#
# print("\n11. While Loop with Else. \n"
#       "Write a program that counts from 1 to 5 using a while loop and prints 'Done!' \n"
#       "in the else block after the loop ends.")
#
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# else:
#     print("Done!")

# # Combining Functions and While Loops
#
# # 12
#
# print("\n12. Password Checker. \n"
#       "Write a function check_password(password) that returns True if the password is 'python123'. \n"
#       "Use a while loop to repeatedly ask the user for the password until they enter the correct one.")
#
# def check_password(password):
#     return password == "python123"
#
# while True:
#     pw = input("Enter password: ")
#     if check_password(pw):
#         print("Access Granted!")
#         break

# # 13
#
# print("\n13. Guess the Number. \n"
#       "Write a function generate_number() that returns a random number between 1 and 10. \n"
#       "to ask the user to guess the number until they get it right.")
#
# def generate_number():
#     return random.randint(1, 10)
#
# target = generate_number()
# print(target)
# while True:
#     guess = int(input("Guess the number: "))
#     if guess == target:
#         print("Congrats!")
#         break
#     else:
#         print("Try again!")

# # 14
#
# print("\n14. Simple Calculator. \n"
#       "Write a function calculate(a, b, operation) that performs addition, \n"
#       "subtraction, or multiplication based on the operation parameter. \n"
#       "Use a while loop to keep asking the user for calculations until they choose to quit.")
#
# def calculate(a, b, operation):
#     if operation == "add" or operation == "a":
#         return a + b
#     if operation == "subtract" or operation == "s":
#         return a - b
#     if operation == "multiply" or operation == "m":
#         return a * b
#     if operation == "divide" or operation == "d":
#         return a / b
#     else:
#         return "Invalid operation"
#
#
# while True:
#     want_calculate = (input("Do you want to use the calculator (yes - no)? "))
#     if want_calculate == "no" or want_calculate == "n":
#         print("Thanks! Goodbye!")
#         break
#     n1 = float(input("Enter the first number: "))
#     n2 = float(input("Enter the second number: "))
#     op = input("Enter the operation (addition, subtraction, multiplication or division): ")
#     result = calculate(n1, n2, op)
#     print(f"The result is: {result}")

# # 15
#
# print("\n15. Prime Number Checker. \n"
#       "Write a function is_prime(n) that returns True if a number is prime and False otherwise, \n"
#       "Use a while loop to allow the user to keep checking numbers until they enter 0")
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# while True:
#     num = int(input("Enter a number to check if is prime or 0 to quit: "))
#     if num == 0:
#         print("Goodbye!")
#         break
#     else:
#         if is_prime(num):
#             print(f"{num} is prime")
#         else:
#             print(f"{num} is not prime")
#
