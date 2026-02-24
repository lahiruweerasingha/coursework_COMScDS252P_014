"""
staff.py

Defines the Staff class extending Person.
Represents administrative or support staff in the university.
"""

from person import Person


class Staff(Person):
    """
    Represents a non-academic staff member.
    """

    def __init__(
        self,
        name: str,
        person_id: str,
        email: str,
        phone: str,
        employee_id: str,
        role: str,
        hire_date: str,
    ):
        super().__init__(name, person_id, email, phone)
        self.employee_id = employee_id
        self.role = role
        self.hire_date = hire_date

    def get_info(self) -> str:
        """
        Extend Person.get_info() with staff details.
        """
        base = super().get_info()
        return (
            f"{base}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Role: {self.role}\n"
            f"Hire Date: {self.hire_date}"
        )

    def get_responsibilities(self) -> str:
        """
        Polymorphism override: staff responsibilities.
        """
        return "Provide administrative support and ensure smooth university operations."