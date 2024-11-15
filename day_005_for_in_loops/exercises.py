# Basic for loops
import random

# Write a program that takes a word as input and prints each character on a new line.
print("\n1. Print Each Character in a String")
word_1 = input("Write a word: ")
for char in word_1:
    print(char)

# Create a list of fruits and print each fruit on a new line.
print("\n2. Print Each Item in a List")
fruits_1 = ["banana", "apple", "kiwi", "pineapple", "mandarin"]
print(f"Fruits: {fruits_1}")
for fruit in fruits_1:
    print(fruit)

# Given a list of words, print each word along with its length
print("\n3. Find the Length of Each Word")
names_1 = ["Bruno", "Taise", "Coralina", "Lila"]
print(f"Names: {names_1}")
for name in names_1:
    print(f"The length of '{name}' is: {len(name)}")

# For Loops with Range

# Use range() to print numbers from 1 to 10.
print("\n4. Print Numbers from 1 to 10")
for num in range(1, 11):
    print(num)

# Use range() to print all even numbers from 2 to 20.
print("\n5. Print Even Numbers from 2 to 20")
for num in range (2, 21):
    if num % 2 == 0:
        print(num)

# Use range() to print numbers from 10 to 1 in descending order, followed by "Liftoff!".
print("\n6. Countdown 10 to 1")
for num in range (10, 0, -1):
    print(num)
print("Liftoff")

# Combining Lists and Loops

# Given a list of names, print each name in uppercase.
print("\n7. Capitalize Each Word")
names_2 = ["bruno", "taise", "coralina", "lila"]
print(f"Names: {names_2}")
for name in names_2:
    print(name.capitalize())

# Use two lists (boys and girls) and pair each boy with a girl.
print("\n8. Match Participants")
boys = ["Nick", "Matt", "Jim"]
girls = ["Ella", "Sue", "Emma"]
print(boys, girls)
for index in range(len(boys)):
    print(f"{boys[index]} is paired with {girls[index]}")

# Using Nested Loops

# Create a 3x3 multiplication table using nested loops.
print("\n9. Print a 3x3 Multiplication Table")
for i in range(1, 4):
    for j in range(1,4):
        print(f"{i} x {j} = {i * j}")

# Given a nested list of student grades, print each student's grades on a new line.
print("\n10. Nested Lists")
grades = [
    [85, 90, 92],
    [78, 88, 85],
    [95, 91, 89]
]
print(f"Grades: {grades}")
for grade in grades:
    print(grade)

#Creative Challenges

# Create a list of 5 random numbers between 1 and 100. Print each number with its index.
print("\n11. Randomized List Printing")

random_numbers =[random.randint(1, 100) for n in range(5)]
print(random_numbers)
for number in random_numbers:
    print(f"The number in index {random_numbers.index(number)} is {number}")

# Given a list of names, print each name in reverse order, along with the reversed name itself.
print("\n12. Reverse Names")
names_3 = ["Bruno", "Taise", "Coralina", "Lila"]
for name in names_3:
    print(f"The name {name} reversed is {''.join(reversed(name))}")