# print("\n1. Comparison Operators\n")
# #Ask the user to enter two numbers.
# # Use comparison operators (==, !=, <, >, <=, >=) to compare them and print the results.
#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# print("Are the numbers equal?", num1 == num2)
# print("Are the numbers not equal?", num1 != num2)
# print("Is the first number less than the second number?", num1 < num2)
# print("Is the first number greater than the second number?", num1 > num2)

# print("\n2. Boolean Operators (and, or, not)\n")
# #Ask the user to enter their age and if they have a driving license (yes/no).
# # Use boolean operators to check if they’re eligible to drive (over 18 and have a license).
#
# age = int(input("Enter your age: "))
# has_license = input("Do you have a driving license (yes/no)? ") == "yes"
# eligible_to_drive = age >= 18 and has_license
# print("Are you eligible to drive?", eligible_to_drive)

# print("\n3. Simple if Statement")
# #Write a program that asks the user for a number and prints "Positive" if the number is greater than zero.
#
# num1 = int(input("Enter a number: "))
# if num1 > 0:
#    print("Positive")

# print("\n4. If-Else Statement")
# #Ask the user for a number and print whether it is positive, negative, or zero.
# num2 = int(input("Enter a number: "))
# if num2 > 0:
#     print(f"{num2} is a positive number")
# else:
#     print(f"{num2} is a either negative or zero")

# print("\n5. If-Elif-Else Statement")
# # Write a program that takes a number from the user and checks if it is positive, negative, or zero using elif.
#
# num3 = int(input("Enter a number: "))
# if num3 > 0:
#     print(f"{num3} is a positive number")
# elif num3 < 0:
#     print(f"{num3} is a negative number")
# else:
#     print(f"{num3} is a zero")

# print("\n6. Nested if Statement")
# # Ask the user for a number. If it’s positive, check if it’s even or odd and print the result.
# num4 = int(input("Enter a number: "))
# if num4 > 0:
#     if num4 % 2 == 0:
#         print(f"{num4} is positive and even")
#     else:
#         print(f"{num4} is positive and odd")
# else:
#     print(f"{num4} is non-positive")

# print("\n7. Ternary Conditional Operator")
# # Ask the user for a number and use a ternary condition to print "Even" or "Odd" based on whether the number is even or odd.
# num5 = int(input("Enter a number: "))
# print(f"{num5} is positive") if num5 > 0 else print(f"{num5} is negative")

# print("\n8. Checking Multiple Conditions with and and or")
# #Write a program that asks the user for two grades. If both grades are above 50, print "Passed", else print "Failed".
#
# grade1 = int(input("Enter the first grade: "))
# grade2 = int(input("Enter the second grade: "))
#
# if grade1 > 50 and grade2 > 50:+
#     print("Passed")
# else:
#     print("Failed")

# print("\n9. Using Multiple Conditions with elif")
# # Ask the user for their grade (0-100). Print "Excellent" for 90-100,
# # "Good" for 75-89, "Average" for 50-74, and "Fail" for below 50.
#
# grade3 = int(input("Enter the grade (0 to 100: ) "))
# if 90 <= grade3 <= 100:
#     print("Excellent")
# elif 75 <= grade3 <= 89:
#     print("Good")
# elif 50 <= grade3 <= 74:
#     print("Average")
# else:
#     print("Fail")
#

# print("10. Basic Switch Case Using Dictionary Mapping")
# #Ask the user for a number from 1 to 3 and print the corresponding day: 1 for "Monday", 2 for "Tuesday", 3 for "Wednesday".
#
# day_number = int(input("Enter a day number (1 to 7): "))
# match day_number:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day number")

# print("11. Using or Pattern in Switch Case")
# # Write a program where the user enters a single letter,
# # and you print whether it’s a vowel or consonant. Use a dictionary for mapping.
#
# single_letter = input("Enter a single letter: ").lower()
# match single_letter:
#     case "a" | "e" | "i" | "o" |"u":
#         print("Its a vowel")
#     case _:
#         print("Its a consonant")
