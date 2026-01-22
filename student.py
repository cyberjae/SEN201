STUDENT RESULT MANAGEMENT SYSTEM
SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC) DOCUMENTATION

(Implementation Included)

1. INTRODUCTION

The Student Result Management System is a console-based software application designed to manage student academic results efficiently. The system allows an administrator or teacher to store student details, enter subject-wise marks, calculate total marks, percentage, and grades, and display student results.

This project follows the Software Development Life Cycle (SDLC) to ensure systematic development, reliability, and maintainability.

2. SDLC PHASES
2.1 REQUIREMENT ANALYSIS
Functional Requirements

Add student details (ID and Name)

Enter subject-wise marks

Calculate:

Total marks

Percentage

Grade

Display stored student results

Persist student data using file storage

Non-Functional Requirements

Easy-to-use console interface

Modular and readable code

Platform-independent

Data consistency and reliability

Users

Admin / Teacher

2.2 FEASIBILITY STUDY
Technical Feasibility

Python provides built-in support for file handling and data processing

JSON ensures simple and lightweight storage

Economic Feasibility

Open-source tools used

No additional cost

Operational Feasibility

Simple console-based interaction

Minimal user training required

2.3 SYSTEM DESIGN
Architecture

Console-based application

File-based storage (JSON)

Module Design (Consistent Nomenclature)
Module Name	Responsibility
Student	Stores student data and grade logic
StudentResultManagementSystem	Handles data storage and retrieval
Main Module	User interaction and execution
Data Design

Student Entity

student_id

name

marks (dictionary)

total

percentage

grade

2.4 TECHNOLOGY STACK

Programming Language: Python 3

Storage: JSON File

OS: Platform Independent

IDE: Any Python-supported IDE

2.5 IMPLEMENTATION
Project Structure
student-result-management-system/
│
├── src/
│   ├── student.py
│   ├── result.py
│   └── main.py
│
├── data/
│   └── students.json

SOURCE CODE
student.py
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.total = sum(marks.values())
        self.percentage = self.total / len(marks)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.percentage >= 90:
            return "A"
        elif self.percentage >= 75:
            return "B"
        elif self.percentage >= 60:
            return "C"
        else:
            return "D"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "marks": self.marks,
            "total": self.total,
            "percentage": self.percentage,
            "grade": self.grade
        }

result.py
import json
from student import Student

class StudentResultManagementSystem:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_student(self, student_id, name, marks):
        student = Student(student_id, name, marks)
        data = self.load_data()
        data.append(student.to_dict())
        self.save_data(data)

    def load_data(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def display_results(self):
        students = self.load_data()
        for s in students:
            print("\nStudent ID:", s["student_id"])
            print("Name:", s["name"])
            print("Marks:", s["marks"])
            print("Total:", s["total"])
            print("Percentage:", s["percentage"])
            print("Grade:", s["grade"])

main.py
from result import StudentResultManagementSystem

system = StudentResultManagementSystem("data/students.json")

while True:
    print("\n--- Student Result Management System ---")
    print("1. Add Student Result")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")

        marks = {}
        subjects = ["Maths", "Science", "English"]
        for subject in subjects:
            marks[subject] = int(input(f"Enter marks for {subject}: "))

        system.add_student(student_id, name, marks)
        print("Student result added successfully!")

    elif choice == "2":
        system.display_results()

    elif choice == "3":
        break
    else:
        print("Invalid choice!")

2.6 TESTING
Testing Method

Manual Testing

Sample Test Cases
Test Case	Input	Expected Result
Add Student	Valid marks	Data saved
Grade Calculation	≥ 90%	Grade A
View Results	Stored data	Correct display
2.7 DEPLOYMENT

Application runs locally

Requires Python 3

No external dependencies

2.8 MAINTENANCE

Future Enhancements:

Database integration

GUI-based interface

User authentication

Result analytics

3. CONCLUSION

The Student Result Management System demonstrates the practical application of SDLC principles. The project ensures structured development, accurate result processing, and efficient data management while remaining simple and scalable
