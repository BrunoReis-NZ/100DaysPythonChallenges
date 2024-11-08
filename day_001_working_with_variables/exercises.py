# 1. Print a Message with print
# Write a program that prints a greeting message.

print("Hello, welcome to Python programming");

# 2. Get User Input and Display It
# Write a program that asks the user for their name and then prints a message saying "Hello, [name]!"

# Option 1
print("Hello" + " " + input("Enter your name: ") + "!")

# Option 2
name = input("Enter your name: ")
print("Hello" + " " + name + "!" )

# 3. String Formatting with f-Strings
# Ask the user for their favorite color and animal,
# and print a sentence like "Your favorite color is [color] and your favorite animal is [animal]."
# Use f-string formatting.

print("Hi" + " " + name + ".")
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print(f"your favorite color is {color} and your favorite animal is a {animal}")

# 4. Concatenate Strings
# Write a program that asks for the user's first name and last name,
# and prints them together as "First Name: [first name], Last Name: [last name]"

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("First name: " + first_name + " , Last name: " + last_name)

# 5. Basic Variable Assignment
# Assign a sentence to a variable, then print that variable.

sentence = "this is a sentence stored in a variable"
print(sentence)

# 6. Using len() Function
# Ask the user for a word, then print the length of that word.

word = input("Type a word that you want to count the length: ")
print(f"the length of '{word}' is {len(word)} characters")

# 7. Using 'end' Keyword in print()
# Print three separate statements on the same line, without spaces between them.
# Experiment with the end keyword.

print("Hello, ", end="")
print("world ", end="")
print("!")

# 8. Using 'sep' Keyword in print()
# Print a list of items separated by commas, without using concatenation.

print("Python", "C#", "Java", "Javascript", sep=" * ")

# 9. Combine len() with User Input
# Ask the user for their full name, and print a message telling them how many characters are in it.

full_name = input("What is your full name? ")
name_without_spaces = full_name.replace(" ", "")
print(f"Your name has {len(name_without_spaces)} characters.")

# 10. Experimenting with f-Strings and sep
# Ask the user for three favorite foods and print them out in one line, separated by a hyphen.

food_1 = input("What is your first favorite food? ")
food_2 = input("What is your second favorite food? ")
food_3 = input("What is your third favorite food? ")
print(food_1, food_2, food_3, sep=" - ")

