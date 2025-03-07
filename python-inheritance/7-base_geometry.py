#!/usr/bin/python3
class BaseGeometry:
    """
    A class used to represent a basic geometric figure.

    Methods:
        area(self): Raises an Exception indicating the area method is not implemented.
        integer_validator(self, name, value): Validates that the value is a positive integer.
    """

    def area(self):
        """
        Raises an Exception with a message indicating that the area method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.

        Args:
            name (str): The name of the variable (for error reporting).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
