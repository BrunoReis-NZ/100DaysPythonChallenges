# Project: Meal Planner
# Goal: Create a program to plan meals for a day based on user preferences.
#
# Requirements:
# Define a Function:
#
# Write a function plan_meal(meal, main_course, side_dish, drink="Water") that prints a meal plan:
# [Meal]: [Main Course], [Side Dish], [Drink]
# Plan the Meals:
#
# Ask the user to input choices for breakfast, lunch, and dinner.
# Use the function to display the planned meals.
# Use Default and Keyword Arguments:
#
# If the user doesn’t specify a drink, use "Water" as the default.

def plan_meal(meal, main_course, side_dish, drink="Water"):
    print(f"[{meal}]: {main_course}, {side_dish}, {drink}")

# Input choices for each meal
breakfast_main = input("Enter the main course for breakfast: ")
breakfast_side = input("Enter the side dish for breakfast: ")
breakfast_drink = input("Enter the drink for breakfast (or press Enter for water): ")

lunch_main = input("Enter the main course for lunch: ")
lunch_side = input("Enter the side dish for lunch: ")
lunch_drink = input("Enter the drink for lunch (or press Enter for water): ")

dinner_main = input("Enter the main course for dinner: ")
dinner_side = input("Enter the side dish for dinner: ")
dinner_drink = input("Enter the drink for dinner (or press Enter for water): ")

# Plan the meals
print("\n--- Meal Plan ---")
plan_meal("Breakfast", breakfast_main, breakfast_side, breakfast_drink or "Water")
plan_meal("Lunch", lunch_main, lunch_side, lunch_drink or "Water")
plan_meal("Dinner", dinner_main, dinner_side, dinner_drink or "Water")
