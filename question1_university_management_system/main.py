"""
main.py

Demonstration script covering requirements A-E:
A) 3 objects of each type + inheritance demo
B) Student enrolls 4–5 courses + grades + GPA + academic status
C) Validation errors (invalid grade, >6 courses)
D) Polymorphism list (Student, Faculty, Staff)
E) 2 departments, 3–4 courses each, assign faculty, enroll students, department summary
"""

from student import Student
from faculty import Faculty
from staff import Staff
from course import Course
from department import Department


def safe_action(label: str, func) -> None:
    try:
        func()
        print(f"[OK] {label}")
    except ValueError as e:
        print(f"[ERROR] {label} -> {e}")


def main() -> None:
    print("\n================ UNIVERSITY MANAGEMENT SYSTEM DEMO ================\n")

    # ---------- A) Create at least 3 objects of each type ----------
    print("A) CLASS HIERARCHY & INHERITANCE\n")

    # Faculty (3)
    fac1 = Faculty("Dr. Silva", "F001", "silva@uni.edu", "0711111111", "EMP1001", "Data Science", "2020-01-15")
    fac2 = Faculty("Dr. Fernando", "F002", "fernando@uni.edu", "0712222222", "EMP1002", "Computer Science", "2019-06-01")
    fac3 = Faculty("Dr. Perera", "F003", "perera@uni.edu", "0713333333", "EMP1003", "Data Science", "2021-03-20")

    # Staff (3)
    staff1 = Staff("Ms. Nuwan", "T001", "nuwan@uni.edu", "0721111111", "STF2001", "Administrator", "Registry")
    staff2 = Staff("Mr. Gayan", "T002", "gayan@uni.edu", "0722222222", "STF2002", "Lab Technician", "Computer Science")
    staff3 = Staff("Ms. Dilani", "T003", "dilani@uni.edu", "0723333333", "STF2003", "Finance Officer", "Finance")

    # Students (3)
    stu1 = Student("Lahiru Weerasingha", "S001", "lahiru@stu.edu", "0712345678", "STU3001", "MSc Data Science", "2026-02-23")
    stu2 = Student("John Perera", "S002", "john@stu.edu", "0723456789", "STU3002", "MSc Data Science", "2026-02-23")
    stu3 = Student("Amaya Silva", "S003", "amaya@stu.edu", "0734567890", "STU3003", "BSc Computer Science", "2026-02-20")

    # Demonstrate method inheritance: update_contact() inherited from Person
    print("Inheritance demo: update_contact() used on Student and Staff\n")
    stu1.update_contact(email="lahiru.weerasingha@stu.edu")
    staff1.update_contact(phone="0770000000")
    print(stu1.get_info(), "\n")
    print(staff1.get_info(), "\n")

    # ---------- E) Create 2 departments with 3–4 courses each ----------
    print("E) DEPARTMENTS + COURSES\n")

    dept_ds = Department("Data Science", dept_head=fac1)
    dept_cs = Department("Computer Science", dept_head=fac2)

    # DS courses (3)
    ds101 = Course("DS101", "Intro to Data Science", 3, instructor=fac1.name, max_capacity=2)
    ds201 = Course("DS201", "Statistics for Data Science", 3, instructor=fac3.name, max_capacity=30)
    ds301 = Course("DS301", "Machine Learning", 4, instructor=fac1.name, max_capacity=30)

    # CS courses (3)
    cs101 = Course("CS101", "Programming Fundamentals", 3, instructor=fac2.name, max_capacity=30)
    cs201 = Course("CS201", "Data Structures", 3, instructor=fac2.name, max_capacity=30)
    cs301 = Course("CS301", "Database Systems", 3, instructor=fac2.name, max_capacity=30)

    for c in [ds101, ds201, ds301]:
        dept_ds.add_course(c)
    for c in [cs101, cs201, cs301]:
        dept_cs.add_course(c)

    dept_ds.add_faculty(fac3)
    dept_cs.add_faculty(fac2)

    print(dept_ds.get_department_info(), "\n")
    print(dept_cs.get_department_info(), "\n")

    # ---------- B) Student enrolls 4–5 courses + grades + status ----------
    print("B) STUDENT COURSE MANAGEMENT\n")

    safe_action("Enroll stu1 in DS101", lambda: ds101.add_student(stu1))
    safe_action("Enroll stu1 in DS201", lambda: ds201.add_student(stu1))
    safe_action("Enroll stu1 in DS301", lambda: ds301.add_student(stu1))
    safe_action("Enroll stu1 in CS101", lambda: cs101.add_student(stu1))
    safe_action("Enroll stu1 in CS201", lambda: cs201.add_student(stu1))

    safe_action("Add grade DS101=3.8", lambda: stu1.add_grade("DS101", 3.8))
    safe_action("Add grade DS201=3.6", lambda: stu1.add_grade("DS201", 3.6))
    safe_action("Add grade DS301=3.4", lambda: stu1.add_grade("DS301", 3.4))
    safe_action("Add grade CS101=3.7", lambda: stu1.add_grade("CS101", 3.7))
    safe_action("Add grade CS201=3.9", lambda: stu1.add_grade("CS201", 3.9))

    print("\nStudent details (GPA + status):\n")
    print(stu1.get_info())

    # ---------- C) Validation & Error Handling ----------
    print("\nC) VALIDATION & ERROR HANDLING\n")
    safe_action("Try invalid grade DS101=4.5", lambda: stu1.add_grade("DS101", 4.5))

    safe_action("Enroll stu1 in CS301 (6th course)", lambda: cs301.add_student(stu1))
    safe_action("Attempt 7th course enrollment (should fail)", lambda: stu1.enroll_course("EXTRA701"))

    print(f"\nGPA is read-only calculated property: {stu1.gpa:.2f}\n")

    # ---------- D) Polymorphism ----------
    print("D) POLYMORPHISM\n")
    people = [stu1, fac1, staff1]
    for p in people:
        print(f"{p.name}: {p.get_responsibilities()}")

    # Extra: Course capacity demo (DS101 max 2)
    print("\nCourse capacity demo (DS101 max 2)\n")
    safe_action("Enroll stu2 in DS101", lambda: ds101.add_student(stu2))
    safe_action("Enroll stu3 in DS101 (should fail)", lambda: ds101.add_student(stu3))

    print("\nCourse status:")
    print(ds101)

    print("\nDepartment summary:")
    print(dept_ds.get_department_info())

    print("\n================ END OF DEMO ================\n")


if __name__ == "__main__":
    main()