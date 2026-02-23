"""
person.py

Defines the base Person class for the University Management System.
This class demonstrates encapsulation and serves as a parent
class for Student, Faculty, and Staff.
"""


class Person:
    """
    Base class representing a person in the university system.
    """

    def __init__(self, name: str, person_id: str, email: str, phone: str):
        """
        Initialize a Person object.

        :param name: Full name of the person
        :param person_id: Unique identifier
        :param email: Email address
        :param phone: Phone number
        """
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

    def update_contact(self, email: str = None, phone: str = None) -> None:
        """
        Update contact details.
        """
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone

    def get_responsibilities(self) -> str:
        """
        Method intended to be overridden by subclasses.
        Demonstrates polymorphism.
        """
        return "General university responsibilities."