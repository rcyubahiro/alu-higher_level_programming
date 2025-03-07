#!/usr/bin/python3
"""
Module containing the Square class that inherits from Rectangle.
The Square class represents a square and includes validation for the size.
It also provides methods for calculating area and printing the square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that represents a square and inherits from Rectangle.
    
    Attributes:
        __size (int): The size of the square (both width and height).
    
    Methods:
        __init__(size): Initializes the square with the given size.
        area(): Returns the area of the square.
        __str__(): Returns a string representation of the square.
        width(): Returns the width of the square.
        height(): Returns the height of the square.
    """

    def __init__(self, size):
        """
        Initializes the square with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be greater than 0")

        self.__size = size
        super().__init__(size, size)  # Passing size for both width and height

    def area(self):
        """
        Returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The square description in the format [Square] size/size.
        """
        return f"[Square] {self.__size}/{self.__size}"

    @property
    def width(self):
        """
        Returns the width of the square.

        Returns:
            int: The width of the square (same as size).
        """
        return self.__size

    @property
    def height(self):
        """
        Returns the height of the square.

        Returns:
            int: The height of the square (same as size).
        """
        return self.__size

