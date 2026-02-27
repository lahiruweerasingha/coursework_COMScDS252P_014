"""
staff.py

Defines the Staff class extending Person.
Represents administrative or support staff in the university.
"""

from person import Person


class Staff(Person):
    """
    Represents a non-academic staff member.
    Adds: employee_id, role, department
    """

    def __init__(
        self,
        name: str,
        person_id: str,
        email: str,
        phone: str,
        employee_id: str,
        role: str,
        department: str,
    ) -> None:
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
        return "Provide administrative support and ensure smooth university operations."