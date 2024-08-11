''' Exercise 1 : Student Grade Summary
Instructions
You are given a dictionary containing student names as keys and lists of their grades as values. Your task is to create a summary report that calculates the average grade for each student, assigns a letter grade, and determines the class average.



Initial Data:


student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}


Requirements:
Calculate the average grade for each student and store the results in a new dictionary called student_averages.
Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale, and store the results in a dictionary called student_letter_grades:
A: 90 and above
B: 80 to 89
C: 70 to 79
D: 60 to 69
F: Below 60
Calculate the class average (the average of all students’ averages) and print it.
Print the name of each student, their average grade, and their letter grade.
Hints:
Use loops to iterate through the student_grades dictionary.
You may use sum() and len() functions to help calculate averages.
Initialize empty dictionaries for student_averages and student_letter_grades before filling them with data.'''

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

# Initialize empty dictionaries
student_averages = {}
student_letter_grades = {}

# Function to determine the letter grade based on the average grade
def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif 80 <= average < 90:
        return "B"
    elif 70 <= average < 80:
        return "C"
    elif 60 <= average < 70:
        return "D"
    else:
        return "F"

# Calculate the average for each student and assign a letter grade
for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    student_averages[student] = average
    student_letter_grades[student] = get_letter_grade(average)

# Calculate the class average
class_average = sum(student_averages.values()) / len(student_averages)

# Print the name of each student, their average grade, and their letter grade
for student in student_grades:
    print(f"{student}: Average Grade = {student_averages[student]:.2f}, Letter Grade = {student_letter_grades[student]}")

# Print the class average
print(f"\nClass Average = {class_average:.2f}")
