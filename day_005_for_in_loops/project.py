# Final Project: Random Number Statistics
# Goal: Create a program that generates a list of random numbers
# and calculates statistics using for loops.
#
# Requirements:
import random

from unicodedata import category

# 1. Generate Random Numbers:
# Generate a list of 10 random integers between 1 and 100.
#
# 2. Print the Numbers:
# Print each number on a new line.
#
# 3. Calculate Statistics:
# Find and print the following:
# - The largest number in the list.
# - The smallest number in the list.
# - The sum of all the numbers.
# - The average of the numbers, formatted to two decimal places.
#
# 4. Additional Challenge:
# Categorize the numbers into "High" (above 50)
# or "Low" (50 and below) and print each number with its category.

print("### Random Number Statistics ###")

# Step one: generate a list of random numbers.

numbers = [random.randint(1, 100) for n in range(10)]

#Step two: print each number on a new line.
#Step three: Calculate Statistics.


largest_number = 0
smallest_number = 100
sum_of_all_numbers = 0
average_of_all_numbers = 0
high_numbers = []
low_numbers = []

print("\n# Random Numbers:")
for number in numbers:
    print(number)
    if number > largest_number:
        largest_number = number
    if number < smallest_number:
        smallest_number = number
    if number > 50:
        high_numbers.append(number)
    else:
        low_numbers.append(number)
    sum_of_all_numbers += number
    average_of_all_numbers = sum_of_all_numbers / 10

print("\n# Statistics:")
print(f"\tLargest number = {largest_number}")
print(f"\tSmallest number = {smallest_number}")
print(f"\tSum of all numbers = {sum_of_all_numbers}")
print(f"\tAverage of all numbers = {average_of_all_numbers: .2f}")

#Step four: Categorize the numbers into "High" (above 50)
# or "Low" (50 and below) and print each number with its category.
print("\n# Categories")

for number in numbers:
    category = "high" if number > 50 else "Low"
    print(f"\t{number}: {category}")





