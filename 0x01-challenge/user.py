#!/usr/bin/env python3
"""A User class with email attribute and property."""

class User(object):
    """A class that represents a user with an email attribute.

    Attributes:
        email (str): The email address of the user.
    """

    def __init__(self):
        """Initialize the user with a private email attribute."""
        self.__email = None

    @property
    def email(self):
        """Get the email address of the user.

        Returns:
            str: The email address of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """Set the email address of the user.

        Args:
            value (str): The new email address of the user.

        Raises:
            TypeError: If value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
