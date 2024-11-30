# Project 1: Employee Management System (Medium Level)
# Scenario: You are tasked to create a simple employee management system. It stores employee details, allows adding new employees, updating existing details, and retrieving employee information.
#
# Requirements:
# Define the System:
# Create a dictionary employees where each key is an employee ID, and the value is another dictionary containing name, age, and department.
#
#Add New Employee:
# Write a function add_employee(employees, emp_id, name, age, department) that adds a new employee.
#
#Update Employee:
# Write a function update_employee(employees, emp_id, key, value) that updates a specific detail of an employee.
#
#Retrieve Employee Details:
# Write a function get_employee(employees, emp_id) that prints all details of an employee.

print("Project 1: Employee Management System (Medium Level)\n")

def add_employee(employees, emp_id, name, age, department):
    employees[emp_id] = {"name": name, "age": age, "department": department}

def update_employee(employees, emp_id, key, value):
    if emp_id in employees:
        employees[emp_id][key] = value
    else:
        print(f"Employee ID {emp_id} not found.")

def get_employee(employees, emp_id):
    if emp_id in employees:
        print(employees[emp_id])
    else:
        print(f"Employee ID {emp_id} not found.")

# Employee dictionary
employees = {}

# Add employees
add_employee(employees, 1, "Alice", 30, "HR")
add_employee(employees, 2, "Bob", 25, "IT")

# Update employee
update_employee(employees, 2, "age", 26)

# Get employee details
get_employee(employees, 1)
get_employee(employees, 2)
