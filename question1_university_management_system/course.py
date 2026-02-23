"""
course.py
Course class for managing student enrollment.
"""

from __future__ import annotations
from student import Student


class Course:
    def __init__(
        self,
        course_code: str,
        course_name: str,
        credits: int,
        instructor: str,
        max_capacity: int = 30,
    ):
        self.course_code = course_code.strip().upper()
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
        self.enrolled_students.append(student)

    def remove_student(self, student: Student) -> None:
        if student not in self.enrolled_students:
            raise ValueError(f"{student.name} is not enrolled in {self.course_code}.")
        self.enrolled_students.remove(student)

    def __str__(self) -> str:
        return f"{self.course_code} - {self.course_name} ({len(self.enrolled_students)}/{self.max_capacity})"