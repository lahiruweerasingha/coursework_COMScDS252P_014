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
    """

    def __init__(self, name: str):
        self.name = name
        self.faculty_members: list[Faculty] = []
        self.courses: list[Course] = []

    def add_faculty(self, faculty: Faculty) -> None:
        """
        Add a faculty member to the department.
        """
        if faculty in self.faculty_members:
            raise ValueError(f"{faculty.name} already exists in {self.name}.")
        self.faculty_members.append(faculty)

    def add_course(self, course: Course) -> None:
        """
        Add a course to the department.
        """
        if course in self.courses:
            raise ValueError(f"{course.course_code} already exists in {self.name}.")
        self.courses.append(course)

    def get_summary(self) -> str:
        """
        Return department summary including courses and faculty.
        """
        faculty_names = ", ".join(f.name for f in self.faculty_members) or "None"
        course_list = ", ".join(c.course_code for c in self.courses) or "None"

        return (
            f"Department: {self.name}\n"
            f"Faculty Members: {faculty_names}\n"
            f"Courses Offered: {course_list}"
        )