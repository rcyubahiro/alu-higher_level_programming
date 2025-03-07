#!/usr/bin/python3
"""
Module that defines a Square class, which is a subclass of Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a Square, subclass of Rectangle."""

    def __init__(self, size):
        """Initialize the square with a size."""
        self.integer_validator("size", size)  # Validate size
        self.__size = size
        super().__init__(self.__size, self.__size)  # Call the Rectangle constructor

    def __str__(self):
        """Return string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
