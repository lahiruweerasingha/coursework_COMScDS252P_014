"""
main.py

Final demonstration script for the University Management System.
Demonstrates:
- Object creation
- Enrollment
- GPA calculation
- Academic status
- Polymorphism
- Course capacity
- Department summary
"""

from student import Student
from faculty import Faculty
from course import Course
from department import Department


def main():

    print("\n================ UNIVERSITY MANAGEMENT SYSTEM DEMO ================\n")

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

    # Create Course
    course1 = Course(
        course_code="DS101",
        course_name="Introduction to Data Science",
        credits=3,
        instructor="Dr. Silva",
        max_capacity=2,
    )

    ds_department.add_course(course1)

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

    # Enroll Students
    course1.add_student(student1)
    course1.add_student(student2)

    student1.enroll_course("DS101")
    student2.enroll_course("DS101")

    # Add Grades
    student1.add_grade("DS101", 3.8)
    student2.add_grade("DS101", 2.5)

    # Display Student Details
    print("----- STUDENT DETAILS -----\n")
    print(student1.get_info())
    print()
    print(student2.get_info())

    # Demonstrate Polymorphism
    print("\n----- RESPONSIBILITIES (Polymorphism) -----\n")
    people = [student1, faculty1]

    for person in people:
        print(f"{person.name}: {person.get_responsibilities()}")

    # Show Course Details
    print("\n----- COURSE DETAILS -----\n")
    print(course1)

    # Show Department Summary
    print("\n----- DEPARTMENT SUMMARY -----\n")
    print(ds_department.get_summary())

    print("\n================ END OF DEMO ================\n")


if __name__ == "__main__":
    main()