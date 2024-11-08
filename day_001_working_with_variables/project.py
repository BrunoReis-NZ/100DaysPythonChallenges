# Small Project: Personal Profile Generator
# Goal: Create a mini "profile generator" that asks the user for some personal information and then displays it as a formatted message.
#
# Instructions:
#
# Ask the user for their first name, last name, age, and favorite hobby.
# Use the len() function to calculate the length of their first and last names combined.
# Display their profile as a formatted message using f-strings, with the end and sep keywords where appropriate.

print("Personal Profile Generator\n")
#Gather information
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = input("What is your age? ")
hobby = input("What is your favorite hobby? ")

#Calculate name length
full_name_length = len(first_name) + len(last_name)

#Display profile information
print("\n--- Profile ---")
print(f"Name: {first_name} {last_name} (Number of characters: {full_name_length}).")
print(f"Age: {age}", end="\n\n")
print(f"Hobby:", hobby, sep=" ")

print(f"Thanks for sharing {first_name}.")