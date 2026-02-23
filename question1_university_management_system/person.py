"""
person.py
Base class for the University Management System.
"""


class Person:
    """
    Base class representing a generic person in the university system.
    """

    def __init__(self, name: str, person_id: str, email: str, phone: str):
        self.name = name
        self.person_id = person_id
        self.email = email
        self.phone = phone

    def get_info(self) -> str:
        """
        Return formatted information about the person.
        """
        return (
            f"Name: {self.name}\n"
            f"Person ID: {self.person_id}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}"
        )

    def update_contact(self, email: str | None = None, phone: str | None = None) -> None:
        """
        Update contact details.
        """
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone

    def get_responsibilities(self) -> str:
        """
        Polymorphism method: overridden in subclasses.
        """
        return "General university responsibilities."