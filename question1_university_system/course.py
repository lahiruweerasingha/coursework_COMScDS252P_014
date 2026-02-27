"""
course.py

Defines the Course class to manage course details and student enrollment.
Includes validation for max capacity and duplicate enrollment.
"""

from __future__ import annotations

from student import Student


class Course:
    """
    Represents a university course.
    Attributes: course_code, course_name, credits, instructor, enrolled_students, max_capacity
    Methods: add_student(), remove_student(), is_full()
    """

    def __init__(
        self,
        course_code: str,
        course_name: str,
        credits: int,
        instructor: str,
        max_capacity: int = 30,
    ) -> None:
        code = course_code.strip().upper()
        if not code:
            raise ValueError("course_code cannot be empty.")
        if int(credits) <= 0:
            raise ValueError("credits must be a positive integer.")
        if int(max_capacity) <= 0:
            raise ValueError("max_capacity must be a positive integer.")

        self.course_code = code
        self.course_name = course_name
        self.credits = int(credits)
        self.instructor = instructor
        self.max_capacity = int(max_capacity)
        self.enrolled_students: list[Student] = []

    def is_full(self) -> bool:
        return len(self.enrolled_students) >= self.max_capacity

    def add_student(self, student: Student) -> None:
        if self.is_full():
            raise ValueError(f"Course {self.course_code} is full.")
        if student in self.enrolled_students:
            raise ValueError(f"{student.name} is already enrolled in {self.course_code}.")

        # Sync Student side enrollment to keep system consistent
        student.enroll_course(self.course_code)

        self.enrolled_students.append(student)

    def remove_student(self, student: Student) -> None:
        if student not in self.enrolled_students:
            raise ValueError(f"{student.name} is not enrolled in {self.course_code}.")
        self.enrolled_students.remove(student)

        if self.course_code in student.enrolled_courses:
            student.enrolled_courses.remove(self.course_code)

    def __str__(self) -> str:
        return (
            f"{self.course_code} - {self.course_name} "
            f"({len(self.enrolled_students)}/{self.max_capacity})"
        )