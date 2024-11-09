# Small Project: Basic Health Assessment
# Goal: Create a program that provides a basic health assessment based on age, BMI, and lifestyle habits.
#
# Instructions:
#
# Ask the user for their age, weight (kg), and height (m).
# Calculate their BMI using weight / (height ** 2).
# Based on their age, assess if they’re a minor or an adult.
# Use BMI to determine if they’re underweight, normal, overweight, or obese:
# BMI < 18.5: Underweight
# 18.5 <= BMI < 24.9: Normal
# 25 <= BMI < 29.9: Overweight
# BMI >= 30: Obese
# Ask if they exercise regularly (yes/no).
# Provide a health message based on all the factors using nested ifs, elif, and ternary conditions.

print("\n--- Basic Health Assessment ---")

# User inputs
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# BMI calculation
bmi = weight / (height ** 2)

# Age group determination
age_group = "Minor" if age < 18 else "Adult"

# BMI category
match (bmi,):
    case (bmi,) if bmi < 18.5:
        bmi_category ="Underweight"
    case (bmi,) if 18.5 <= bmi <= 24.9:
        bmi_category = "Normal"
    case (bmi, ) if 25 <= bmi <= 29.9:
        bmi_category = "Overweight"
    case (bmi, ) if bmi >= 30:
        bmi_category = "Obese"

# Exercise routine
exercise = input("Do you exercise regularly (Yes or No? ").strip().lower()
exercising = exercise == "yes"

# Health message
print("\n--- Health Assessment ---")
print(f"Name: {name}")
print(f"Age: {age} ({age_group})")
print(f"BMI: {bmi:.2f} ({bmi_category})")
print(f"Exercise regularly: {exercise}")

# Final health suggestion
if age_group == "Minor":
    if bmi_category != "Normal":
        print("Suggestion: Consider consulting with a healthcare provider for guidance.")
    else:
        print("Suggestion: Keep up the good habits!")
elif age_group == "Adult":
    if bmi_category == "Normal" and exercising:
        print("Suggestion: Great job! Maintain a balanced lifestyle.")
    elif bmi_category == "Overweight" or bmi_category == "Obese":
        print("Suggestion: Try to adopt a healthier diet and regular exercise.")
    elif not exercising:
        print("Suggestion: Consider starting a regular exercise routine.")