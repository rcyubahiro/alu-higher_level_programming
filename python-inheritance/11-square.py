#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Initialization with size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be greater than 0")
        
        self.__size = size
        # Initialize the Rectangle with the same size for width and height
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    @property
    def width(self):
        return self.__size

    @property
    def height(self):
        return self.__size
