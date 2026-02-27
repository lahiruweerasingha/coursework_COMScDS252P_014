"""
department.py

Defines the Department class.
Manages faculty members and courses within a department.
"""

from faculty import Faculty
from course import Course


class Department:
    """
    Represents a university department.

    Attributes:
        dept_name, dept_head, faculty_list, course_list
    Methods:
        add_faculty(), add_course(), get_department_info()
    """

    def __init__(self, dept_name: str, dept_head: Faculty | None = None) -> None:
        self.dept_name = dept_name
        self.dept_head = dept_head
        self.faculty_list: list[Faculty] = []
        self.course_list: list[Course] = []

        if dept_head is not None:
            self.add_faculty(dept_head)

    def add_faculty(self, faculty: Faculty) -> None:
        if faculty in self.faculty_list:
            raise ValueError(f"{faculty.name} already exists in {self.dept_name}.")
        self.faculty_list.append(faculty)

    def add_course(self, course: Course) -> None:
        if course in self.course_list:
            raise ValueError(f"{course.course_code} already exists in {self.dept_name}.")
        self.course_list.append(course)

    def get_department_info(self) -> str:
        head = self.dept_head.name if self.dept_head else "None"
        faculty_names = ", ".join(f.name for f in self.faculty_list) or "None"
        course_codes = ", ".join(c.course_code for c in self.course_list) or "None"

        return (
            f"Department: {self.dept_name}\n"
            f"Department Head: {head}\n"
            f"Faculty List: {faculty_names}\n"
            f"Course List: {course_codes}"
        )