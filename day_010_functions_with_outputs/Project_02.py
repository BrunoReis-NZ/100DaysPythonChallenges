# Project 2: Student Grades System (Intermediate Level)
# Scenario: Create a system that calculates the average and highest grade for a student.
#
# Requirements:
#
# Write a function calculate_grades(grades) that returns the average grade and the highest grade.
# Allow the user to input grades as a comma-separated string.
# Use the function to calculate and display the average and highest grade.


print("\nStudent Grades System\n")


def calculate_grades(grades):
    highest_grade = max(grades)
    average_grade = sum(grades)/len(grades)
    return highest_grade, average_grade




calculate_again = True

while calculate_again == True:
    grades_input = input("\nEnter grades separated by commas: ")
    grades = list(map(int, grades_input.split(',')))

    highest, average = calculate_grades(grades)
    print(f"The average of 'grades' is: {average: .2f}")
    print(f"The highest of 'grades' is: {highest}")

    choose = input("\nDo you want to calculate grades again (yes/no)? ")

    if choose == "no":
        calculate_again = False
        print("Goodbye")
