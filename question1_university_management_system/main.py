from person import Person
from student import Student
from faculty import Faculty
from staff import Staff
from course import Course
from department import Department


def demo_q1():
    print("=== A) Class Hierarchy & Inheritance Demo ===")

    # Create 3 Students
    s1 = Student("Alice Smith", "P001", "alice@uni.com", "0711111111", "S1001", "Data Science", "2025-01-10")
    s2 = Student("Bob Lee", "P002", "bob@uni.com", "0722222222", "S1002", "Computer Science", "2025-01-12")
    s3 = Student("Chamara Perera", "P003", "chamara@uni.com", "0733333333", "S1003", "AI", "2025-01-15")

    # Create 3 Faculty
    f1 = Faculty("Dr. Silva", "P101", "silva@uni.com", "0777777777", "E9001", "Computing", "2020-06-01")
    f2 = Faculty("Dr. Fernando", "P102", "fernando@uni.com", "0788888888", "E9002", "Computing", "2019-02-15")
    f3 = Faculty("Prof. Jayasinghe", "P103", "jay@uni.com", "0799999999", "E9003", "Business", "2018-09-10")

    # Create 3 Staff
    st1 = Staff("Nimal", "P201", "nimal@uni.com", "0700000001", "E8001", "Admin Officer", "Registry")
    st2 = Staff("Kamal", "P202", "kamal@uni.com", "0700000002", "E8002", "Lab Technician", "Computing")
    st3 = Staff("Sunil", "P203", "sunil@uni.com", "0700000003", "E8003", "Librarian", "Library")

    print("\n--- Inherited get_info() examples ---")
    print(s1.get_info())
    print()
    print(f1.get_info())
    print()
    print(st1.get_info())

    print("\n=== B) Student Course Management Demo ===")
    # Student enrolls in 4-5 courses
    for code in ["CS101", "DS102", "AI103", "MA104", "ST105"]:
        s1.enroll_course(code)

    # Add grades
    s1.add_grade("CS101", 3.7)
    s1.add_grade("DS102", 3.9)
    s1.add_grade("AI103", 3.2)
    s1.add_grade("MA104", 3.4)
    s1.add_grade("ST105", 3.8)

    print(s1.get_info())

    print("\n=== C) Encapsulation & Data Validation Demo (Show Errors) ===")
    try:
        s1.add_grade("CS101", 4.5)  # invalid grade
    except ValueError as e:
        print(f"Caught error (invalid grade): {e}")

    try:
        # Attempt to exceed max 6 courses
        s1.enroll_course("EX106")
        s1.enroll_course("EX107")  # should fail (7th course)
    except ValueError as e:
        print(f"Caught error (max courses): {e}")

    print("\n=== D) Polymorphism Demo (get_responsibilities) ===")
    people = [s2, f2, st2, s3, f3, st3]
    for p in people:
        print(f"{p.name} -> {p.get_responsibilities()}")

    print("\n=== E) Course & Department Classes Demo ===")

    # Create courses
    c1 = Course("CS101", "Programming Fundamentals", 3, instructor=f1.name, max_capacity=2)
    c2 = Course("DS102", "Intro to Data Science", 3, instructor=f2.name, max_capacity=3)
    c3 = Course("AI103", "AI Basics", 3, instructor=f2.name, max_capacity=3)
    c4 = Course("BU201", "Business Analytics", 3, instructor=f3.name, max_capacity=3)

    # Create departments (2)
    d1 = Department("Computing", dept_head=f1)
    d2 = Department("Business", dept_head=f3)

    # Add faculty
    d1.add_faculty(f1)
    d1.add_faculty(f2)
    d2.add_faculty(f3)

    # Add courses (3-4 each)
    d1.add_course(c1)
    d1.add_course(c2)
    d1.add_course(c3)
    d2.add_course(c4)

    # Enroll students into courses (Course class + Student enrollments)
    # We do both: Student enroll_course AND Course add_student
    s2.enroll_course("CS101")
    c1.add_student(s2)

    s3.enroll_course("CS101")
    c1.add_student(s3)

    # This will fail because max_capacity=2
    try:
        s1.enroll_course("CS101")
        c1.add_student(s1)
    except ValueError as e:
        print(f"Caught error (course full): {e}")

    print("\n--- Department summaries ---")
    print(d1.get_department_info())
    print()
    print(d2.get_department_info())

    print("\n--- Course summaries ---")
    for course in [c1, c2, c3, c4]:
        print(course)


if __name__ == "__main__":
    demo_q1()