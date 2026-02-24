"""
main.py

Demonstration script for the University Management System.
Shows object creation, enrollment, GPA calculation,
polymorphism, and department management.
"""

from student import Student
from faculty import Faculty
from staff import Staff
from course import Course
from department import Department


def main():

    # Create Department
    ds_department = Department("Data Science")

    # Create Faculty
    faculty1 = Faculty(
        name="Dr. Silva",
        person_id="F001",
        email="silva@university.edu",
        phone="0711111111",
        employee_id="EMP1001",
        department="Data Science",
        hire_date="2020-01-15",
    )

    ds_department.add_faculty(faculty1)

    # Create Courses
    course1 = Course("DS101", "Introduction to Data Science", 3, "Dr. Silva", max_capacity=2)
    course2 = Course("ML201", "Machine Learning", 4, "Dr. Silva", max_capacity=2)

    ds_department.add_course(course1)
    ds_department.add_course(course2)

    # Create Students
    student1 = Student(
        name="Lahiru Weerasingha",
        person_id="S001",
        email="COMScDS252P-014@student.nibm.lk",
        phone="0712345678",
        student_id="COMScDS252P-014",
        major="MSc Data Science",
        enrollment_date="2026-02-23",
    )

    student2 = Student(
        name="John Perera",
        person_id="S002",
        email="john@student.nibm.lk",
        phone="0723456789",
        student_id="COMScDS252P-015",
        major="MSc Data Science",
        enrollment_date="2026-02-23",
    )

    # Enroll Students in Courses
    course1.add_student(student1)
    course1.add_student(student2)

    student1.enroll_course("DS101")
    student2.enroll_course("DS101")

    # Add Grades
    student1.add_grade("DS101", 3.8)
    student2.add_grade("DS101", 2.5)

    # Display Student Information
    print("----- STUDENT DETAILS -----")
    print(student1.get_info())
    print()
    print(student2.get_info())

    # Demonstrate Polymorphism
    print("\n----- RESPONSIBILITIES -----")
    people = [student1, faculty1]

    for person in people:
        print(f"{person.name}: {person.get_responsibilities()}")

    # Display Course Info
    print("\n----- COURSE DETAILS -----")
    print(course1)

    # Display Department Summary
    print("\n----- DEPARTMENT SUMMARY -----")
    print(ds_department.get_summary())


if __name__ == "__main__":
    main()