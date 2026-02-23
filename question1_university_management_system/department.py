"""
department.py
Department class to manage faculty and courses.
"""

from __future__ import annotations
from faculty import Faculty
from course import Course


class Department:
    def __init__(self, dept_name: str, dept_head: Faculty):
        self.dept_name = dept_name
        self.dept_head = dept_head
        self.faculty_list: list[Faculty] = []
        self.course_list: list[Course] = []

    def add_faculty(self, faculty: Faculty) -> None:
        if faculty in self.faculty_list:
            raise ValueError(f"{faculty.name} is already in {self.dept_name}.")
        self.faculty_list.append(faculty)

    def add_course(self, course: Course) -> None:
        if course in self.course_list:
            raise ValueError(f"{course.course_code} already exists in {self.dept_name}.")
        self.course_list.append(course)

    def get_department_info(self) -> str:
        faculty_names = ", ".join([f.name for f in self.faculty_list]) if self.faculty_list else "None"
        course_codes = ", ".join([c.course_code for c in self.course_list]) if self.course_list else "None"

        return (
            f"Department: {self.dept_name}\n"
            f"Head: {self.dept_head.name}\n"
            f"Faculty: {faculty_names}\n"
            f"Courses: {course_codes}"
        )