"""
student.py

Defines the Student class which extends Person.
Includes course enrollment, grade management, GPA calculation,
academic status evaluation, and data validation.
"""

from __future__ import annotations

from person import Person


class Student(Person):
    """
    Represents a student in the university system.
    """

    MAX_COURSES_PER_SEMESTER = 6

    def __init__(
        self,
        name: str,
        person_id: str,
        email: str,
        phone: str,
        student_id: str,
        major: str,
        enrollment_date: str,
    ) -> None:
        super().__init__(name, person_id, email, phone)

        self.student_id = student_id
        self.major = major
        self.enrollment_date = enrollment_date

        self.enrolled_courses: list[str] = []
        self._grades: dict[str, float] = {}

    def enroll_course(self, course_code: str) -> None:
        """
        Add course to enrolled list (max 6 courses).
        """
        code = course_code.strip().upper()
        if not code:
            raise ValueError("Course code cannot be empty.")

        if code in self.enrolled_courses:
            raise ValueError(f"Already enrolled in {code}.")

        if len(self.enrolled_courses) >= self.MAX_COURSES_PER_SEMESTER:
            raise ValueError(
                f"Cannot enroll in more than {self.MAX_COURSES_PER_SEMESTER} courses per semester."
            )

        self.enrolled_courses.append(code)

    def add_grade(self, course_code: str, grade: float) -> None:
        """
        Record a grade for a course (0.0–4.0).
        """
        code = course_code.strip().upper()

        if code not in self.enrolled_courses:
            raise ValueError(f"Cannot add grade: not enrolled in {code}.")

        if not (0.0 <= float(grade) <= 4.0):
            raise ValueError("Grade must be between 0.0 and 4.0.")

        self._grades[code] = float(grade)

    def calculate_gpa(self) -> float:
        """
        Calculate GPA from recorded grades.
        """
        if not self._grades:
            return 0.0
        return sum(self._grades.values()) / len(self._grades)

    @property
    def gpa(self) -> float:
        """
        Read-only GPA property.
        """
        return self.calculate_gpa()

    @property
    def grades(self) -> dict[str, float]:
        """
        Read-only view of grades dictionary.
        """
        return dict(self._grades)

    def get_academic_status(self) -> str:
        """
        Academic status:
        - Dean's List (>= 3.5)
        - Good Standing (>= 2.0)
        - Probation (< 2.0)
        """
        if self.gpa >= 3.5:
            return "Dean's List"
        if self.gpa >= 2.0:
            return "Good Standing"
        return "Probation"

    def get_responsibilities(self) -> str:
        """
        Polymorphism override.
        """
        return "Attend lectures, complete coursework, sit exams, and follow academic integrity rules."

    def get_info(self) -> str:
        """
        Extend Person.get_info() with student details.
        """
        base = super().get_info()
        courses = ", ".join(self.enrolled_courses) if self.enrolled_courses else "None"

        return (
            f"{base}\n"
            f"Student ID: {self.student_id}\n"
            f"Major: {self.major}\n"
            f"Enrollment Date: {self.enrollment_date}\n"
            f"Enrolled Courses: {courses}\n"
            f"GPA: {self.gpa:.2f}\n"
            f"Academic Status: {self.get_academic_status()}"
        )