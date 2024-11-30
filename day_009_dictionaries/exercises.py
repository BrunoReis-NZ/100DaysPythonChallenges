# Basic Dictionary Operations

# 1
print("\n1. Create a Dictionary. \n"
      "Create a dictionary person with keys: name, age, and city. Assign values to each key and print the dictionary.")

person = {}
person = {
    "Name": "Bruno",
    "Age": 47,
    "City": "Wellington",
}

print(person)

# 2
print("\n2. Retrieve Items from a Dictionary. \n"
      "Access and print the name and city from the dictionary created above.")

print(f"The student {person["Name"]} is {person["Age"]} years old and lives in {person["City"]}.")

# 3
print("\n3. Add a New Item to a Dictionary \n"
      "Add a new key-value pair job: \"Software Engineer\" to the dictionary and print it..")

person["Job"] = "Software Engineer"

print(f"The student {person["Name"]} is {person["Age"]} years old and lives in {person["City"]} and he is an {person["Job"]}.")

# 4
print("\n4. Edit an Existing Value \n"
      "Update the city value to \"Porirua\" and print the dictionary.")

person["City"] = "Porirua"

print(f"The student {person["Name"]} is {person["Age"]} years old and lives in {person["City"]} and he is an {person["Job"]}.")

# 5
print("\n5. Check for a Key \n"
      "Check if the key age exists in the dictionary. If it does, print its value.")

if "Age" in person:
    print(person["Age"])

# Looping Through Dictionaries

# 6
print("\n6. Loop Through Keys. \n"
      "Loop through the dictionary person and print each key.")

for key in person.keys():
    print(key)

#or...

for key in person:
    print(key)

# 7
print("\n7. Loop Through Values. \n"
      "Loop through the dictionary person and print each Value.")

for value in person.values():
    print(value)

#or...

for key in person:
    print(person[key])

# 8
print("\n8. Loop Through Keys and Values. \n"
      "Loop through the dictionary person and print both the key and value.")

for key, value in person.items():
    print(f"{key} : {value}")

# Nested Lists and Dictionaries

# 9
print("\n9. List Nested in a Dictionary. \n"
      "Create a dictionary student with keys name and subjects. \n"
      "Assign a list of subjects (Math, Science, History) to the subjects key. \n"
      "Print the dictionary..")

student = {}
student = {
    "Name": "Bruno",
    "Subject": ["Java", "Python", "C#"],
}

print(student)

# 10
print("\n10. Access Nested List. \n"
      "Print the second subject from the subjects list in the student dictionary")

print(student["Subject"][1])

# 11
print("\n11. Dictionary Nested in a Dictionary. \n"
      "Create a dictionary company with keys name, location, and departments. \n"
      "The departments key should contain another dictionary with department names (HR, IT) as keys and employee counts as values.")


company = {}
company = {
    "Name": "Hy Brazil",
    "Location": "Wellington",
    "Departments": {
        "HR": 5,
        "IT": 12,
    }
}
print(company)

# 12
print("\n12. Access Nested Dictionary. \n"
      "Print the number of employees in the IT department from the company dictionary.")

print(f"The number of employees in the IT departments is: {company["Departments"]["IT"]}")

# 13
print("\n13. Edit Nested Dictionary. \n"
      "Update the number of employees in the HR department to 15.")

company["Departments"]["IT"] = 15
print(f"The number of employees in the IT departments is: {company["Departments"]["IT"]}")

# Advanced Dictionary Manipulations

# 14
print("\n14. Add an Item to a Nested List. \n"
      "Add a new subject (Art) to the subjects list in the student dictionary and print it.")

student["Subject"].append("Javascript")
print(student)

# 15
print("\n15. Add a New Nested Dictionary. \n"
      "Add a new department (Sales: 20 employees) to the departments dictionary inside company.")

company["Departments"] ["Sales"] = 20
print(company["Departments"])

# 16
print("\n16. Loop Through Nested Dictionary. \n"
      "Loop through the departments dictionary in company and print each department and its employee count.")

for department, employees_count in company["Departments"].items():
    print(f"{department} : {employees_count} employees")

#or...

for department in company["Departments"]:
    print(f"{department} : {company["Departments"][department]} employees")




