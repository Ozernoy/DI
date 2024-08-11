'''
Exercise: Implementing a Student Grade Management System
In this exercise, you'll create a system to manage student grades. The system will allow you to add students, record their grades for different subjects, calculate their average grades, and display student information. You will use dictionaries to store the grades for each subject.
Step-by-Step Instructions:
1. *Define the Student Class:*
   - Create a class called Student.
   - In the __init__ method, define two attributes: name (the name of the student) and grades (a dictionary to hold the subjects as keys and the corresponding grades as values).
2. *Create a Method to Add or Update Grades:*
   - Define a method called add_grade that accepts a subject and a grade as parameters.
   - The method should add the subject and grade to the grades dictionary or update the grade if the subject already exists.
3. *Create a Method to Calculate the Average Grade:*
   - Define a method called calculate_average that calculates and returns the average grade across all subjects.
4. *Override the __str__ Method:*
   - Customize the string representation of the Student class to display the student's name and their grades in each subject.
5. *Define the Gradebook Class:*
   - Create a class called Gradebook.
   - In the __init__ method, define an attribute called students, which should be an empty list that will hold Student objects.
6. *Create a Method to Add a Student:*
   - Define a method called add_student that accepts a Student object and adds it to the students list.
7. *Create a Method to Find a Student by Name:*
   - Define a method called find_student that accepts a student's name and returns the Student object if found. If not found, return a message indicating that the student is not in the gradebook.
8. *Create a Method to Display All Students' Information:*
   - Define a method called display_all_students that prints the information of all students using their string representation.
9. *Test the Classes:*
   - Create instances of the Student class and add them to a Gradebook instance.
   - Add or update grades for each student.
   - Calculate the average grades and display all students' information.
Challenge Additions:
- *Add a Remove Grade Feature:* Implement a method in the Student class to remove a grade for a specific subject.
- *Advanced Search:* Modify the find_student method in the Gradebook class to handle partial matches (e.g., searching for "Ali" should find "Alice").
- *Class Rank:* Implement a method in the Gradebook class to rank students based on their average grades.
12:11
https://colab.research.google.com/drive/1tfxBc8fge4XEFXqGkalHfZcVJINsKEWC?usp=sharing
colab.research.google.comcolab.research.google.com
Google Colab (5 kB)
https://colab.research.google.com/drive/1tfxBc8fge4XEFXqGkalHfZcVJINsKEWC?usp=sharing

New
12:13
# Usage Example
student1 = Student("Alice")
student2 = Student("Bob")
gradebook = Gradebook()
gradebook.add_student(student1)
gradebook.add_student(student2)
student1.add_grade("Math", 90)
student1.add_grade("English", 85)
student2.add_grade("Math", 78)
student2.add_grade("Science", 88)
print(f"{student1.name}'s average grade: {student1.calculate_average()}")
print(f"{student2.name}'s average grade: {student2.calculate_average()}")
gradebook.display_all_students()
Output:
Alice's average grade: 87.5
Bob's average grade: 83.0
Alice - Grades: Math: 90, English: 85
Bob - Grades: Math: 78, Science: 88

'''