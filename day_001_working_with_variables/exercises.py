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
