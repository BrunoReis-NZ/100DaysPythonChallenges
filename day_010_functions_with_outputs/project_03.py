# Project 3: Employee Payroll System (Advanced Level)
# Scenario: Create a payroll system that calculates an employee's total pay based on their hourly rate, hours worked, and any bonuses.
#
# Requirements:
#
# Write a function calculate_pay(hours, rate, bonus=0) that returns the total pay.
# Use a dictionary to store employee details (name, hours, rate, bonus).
# Use the function to calculate and display each employee's total pay.


def calculate_pay(hours, rate, bonus=0):
    return hours * rate + bonus

#4 employees
employees = {
    "Bruno": {"Hours": 40, "Rate": 20, "Bonus": 100},
    "John": {"Hours": 30, "Rate": 15, "Bonus": 50},
    "Jane": {"Hours": 35, "Rate": 18, "Bonus": 75},
    "Alice": {"Hours": 45, "Rate": 25, "Bonus": 150},
}

for name, details in employees.items():
    total_pay = calculate_pay(details["Hours"], details["Rate"], details["Bonus"])
    print(f"{name}'s total pay is ${total_pay: .2f}")
