# Tip Calculator
# Goal: Create a tip calculator that calculates the amount each person needs to pay.
# Instructions:
# Print a welcome message.
# Ask the user for the total bill.
# Ask the user for the percentage tip they would like to give (10%, 12%, or 15%).
# Ask the user for the number of people to split the bill.
# Calculate the amount each person needs to pay, including the tip.
# Display the final amount each person needs to pay.
# Use the round() function to ensure the result has two decimal places.
# Use string interpolation to display the final amount.


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

individual_bill = round((bill / people * (tip / 100 + 1)), 2)

print(f"Each person should pay ${individual_bill}")

#This challenge is a simple exercise to practice basic arithmetic operations and string interpolation.
#The user is asked to input the total bill, the percentage tip, and the number of people to split the bill.
#The program calculates the amount each person needs to pay, including the tip, and displays the result using string interpolation.
#The round() function is used to ensure the final amount has two decimal places.
#The program is structured with a welcome message, input prompts, the calculation, and the final output.

