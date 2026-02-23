"""
faculty.py
Faculty class derived from Person.
"""

from person import Person


class Faculty(Person):
    def __init__(
        self,
        name: str,
        person_id: str,
        email: str,
        phone: str,
        employee_id: str,
        department: str,
        hire_date: str,
    ):
        super().__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.department = department
        self.hire_date = hire_date

    def get_info(self) -> str:
        base = super().get_info()
        return (
            f"{base}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Department: {self.department}\n"
            f"Hire Date: {self.hire_date}"
        )

    def get_responsibilities(self) -> str:
        return "Teach courses, supervise students, conduct research, and contribute to academic service."