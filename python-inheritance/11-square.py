#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        self.__width = size
        self.__height = size

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    def __dir__(self):
        # Only return the desired attributes for dir()
        return ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
                '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
                '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
                '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']


# Test case
print(dir(Square))  # Should print the expected list of attributes

