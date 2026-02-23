"""
student.py
Student class with course enrollment, grading, GPA calculation, and validation.
"""

from __future__ import annotations
from person import Person


class Student(Person):
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
    ):
        super().__init__(name, person_id, email, phone)
        self.student_id = student_id
        self.major = major
        self.enrollment_date = enrollment_date

        self.enrolled_courses: list[str] = []
        self._grades: dict[str, float] = {}  # course_code -> grade (0.0 - 4.0)

    def enroll_course(self, course_code: str) -> None:
        """
        Enroll in a course code, with max course limit validation.
        """
        course_code = course_code.strip().upper()

        if course_code in self.enrolled_courses:
            raise ValueError(f"Already enrolled in {course_code}.")

        if len(self.enrolled_courses) >= self.MAX_COURSES_PER_SEMESTER:
            raise ValueError(
                f"Cannot enroll in more than {self.MAX_COURSES_PER_SEMESTER} courses per semester."
            )

        self.enrolled_courses.append(course_code)

    def add_grade(self, course_code: str, grade: float) -> None:
        """
        Add a grade for an enrolled course. Grade must be between 0.0 and 4.0.
        """
        course_code = course_code.strip().upper()

        if course_code not in self.enrolled_courses:
            raise ValueError(f"Cannot add grade. Student not enrolled in {course_code}.")

        if not (0.0 <= grade <= 4.0):
            raise ValueError("Grade must be between 0.0 and 4.0.")

        self._grades[course_code] = float(grade)

    def calculate_gpa(self) -> float:
        """
        Calculate cumulative GPA from recorded grades.
        If no grades exist yet, return 0.0.
        """
        if not self._grades:
            return 0.0
        return sum(self._grades.values()) / len(self._grades)

    @property
    def gpa(self) -> float:
        """
        Read-only GPA property (calculated, cannot be directly set).
        """
        return self.calculate_gpa()

    def get_academic_status(self) -> str:
        """
        Return academic status based on GPA.
        """
        if self.gpa >= 3.5:
            return "Dean's List"
        if self.gpa >= 2.0:
            return "Good Standing"
        return "Probation"

    def get_info(self) -> str:
        """
        Extend base info with student details.
        """
        base = super().get_info()
        return (
            f"{base}\n"
            f"Student ID: {self.student_id}\n"
            f"Major: {self.major}\n"
            f"Enrollment Date: {self.enrollment_date}\n"
            f"Courses Enrolled: {', '.join(self.enrolled_courses) if self.enrolled_courses else 'None'}\n"
            f"GPA: {self.gpa:.2f} ({self.get_academic_status()})"
        )

    def get_responsibilities(self) -> str:
        """
        Polymorphism override.
        """
        return "Attend lectures, complete assignments, sit exams, and maintain academic integrity."