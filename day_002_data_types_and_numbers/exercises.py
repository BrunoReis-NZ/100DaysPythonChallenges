print("1. Basic Data Types and Type Checking")
# Create variables of type str, int, float, and bool.
# Print each variable and its type using the type() function.

name = "Bruno"
age = 47
weight = 100.5
is_student = True

print(name, type(name), sep= " - ")
print(age, type(age), sep= " - ")
print(weight, type(weight), sep=" - ")
print(is_student, type(is_student), sep= " - ")

print("\n2. Type Conversion")
# Ask the user for their age as a string, then convert it to an integer and print the result.

age_str = input("What is your age? ")
age_int = int(age_str)
print("In five years you will be", age_int + 5, "years old")

print("\n3. Basic Math Operations")
# Write a program that asks for two numbers, then prints their sum, difference, product, and quotient.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", int(num1) + int(num2))
print("Difference:", int(num1) - int(num2))
print("Product:", int(num1) * int(num2))
print("Quotient:", int(num1) / int(num2))

print("\n4. Number Manipulation with Power and Modulus")
# Ask the user for a base and an exponent, then print the result of raising the base to that exponent.
# Also, print the modulus of two numbers.

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent number: "))
print("Result of raising the base to the exponent:", base ** exponent)
print("Modulus of the two numbers:", base % exponent)

print("\n5. Assignment Operators")
# Set a variable to 100, then use +=, -=, *=, and /= to change its value.
# Print the value after each operation.

number_to_be_assigned = int(input("Enter a number: "))
print(f"Number: {number_to_be_assigned}")
number_to_be_assigned += 10
print("After += 10:", number_to_be_assigned)
number_to_be_assigned -= 5
print("After -= 5:", number_to_be_assigned)
number_to_be_assigned *= 2
print("After *= 2:", number_to_be_assigned)
number_to_be_assigned /= 3
print("After /= 3:", number_to_be_assigned)

print("\n6. Subscripting")
# Ask the user to enter a word, then print the first, middle, and last characters of the word.

word = input("Enter a word: ")
middle_index = len(word) // 2
print("First character:", word[0])
print("Middle character:", word[middle_index])
print("Last character:", word[-1])

print("\n7. Using Math Functions")
# Ask the user for a number, then print its absolute value, square root, and rounded value.

import math
num = float(input("Enter a number: "))
print(f"Absolute value: {abs(num)}")
print(f"Square root: {math.sqrt(abs(num))}")
print(f"floor number: {math.floor(num)}")
print(f"ceil number: {math.ceil(num)}")

print("\n8. Formatting Numbers")
# Ask the user for a large number,
# then format it with commas and display it as currency with two decimal places.

large_number = float(input("Enter a large, decimal number: "))
print("Formatted:", f"${large_number:,.2f}")

print("\n9. Using Boolean Expressions")
# Ask the user for their age, then print whether they are a teenager (age between 13 and 19) or not.

age2 = int(input("Enter your age: "))
is_teenager = age2 >= 13 and age2 <= 19
print(f"Are you a teenager? {is_teenager}")

print("\n10. Combining Strings and Numbers")
# Ask the user for their birth year and current year, then calculate and print their age in a formatted message.

birth_year = int(input("Enter your birth year? "))
current_year = int(input("Enter your birth year? "))
age = current_year - birth_year
print(f"You are {age} years old.")
