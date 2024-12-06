# Projects
# Project 1: Simple Calculator (Beginner Level)
# Scenario: Create a calculator that performs basic arithmetic operations.
#
# Requirements:
#
# Write a function calculate(a, b, operation) that takes two numbers and an operation (add, subtract, multiply, divide) and returns the result.
# Allow the user to input two numbers and an operation.
# Use the function to display the result.

def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

calculate_again = True

while calculate_again:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")
    result = calculate(a, b, operation)
    print(f"Result: {result}")
    choice = input("Do you want to do another calculation (yes or no)? ")
    if choice == "no":
        calculate_again = False
        print("Goodbye!")


