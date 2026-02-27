"""
faculty.py

Defines the Faculty class extending Person.
Represents academic staff responsible for teaching and research.
"""

from person import Person


class Faculty(Person):
    """
    Represents a faculty member in the university system.
    Adds: employee_id, department, hire_date
    """

    def __init__(
        self,
        name: str,
        person_id: str,
        email: str,
        phone: str,
        employee_id: str,
        department: str,
        hire_date: str,
    ) -> None:
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
        return "Deliver lectures, supervise students, conduct research, and contribute to academic development."