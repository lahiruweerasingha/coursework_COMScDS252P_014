"""
staff.py
Staff class derived from Person.
"""

from person import Person


class Staff(Person):
    def __init__(
        self,
        name: str,
        person_id: str,
        email: str,
        phone: str,
        employee_id: str,
        role: str,
        department: str,
    ):
        super().__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.role = role
        self.department = department

    def get_info(self) -> str:
        base = super().get_info()
        return (
            f"{base}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Role: {self.role}\n"
            f"Department: {self.department}"
        )

    def get_responsibilities(self) -> str:
        return f"Provide operational support and execute role duties as a {self.role} in {self.department}."