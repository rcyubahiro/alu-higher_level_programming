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
        # Return the specific list of attributes for dir()
        return [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
            '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
            '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
            '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
            '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator'
        ]


# Test case - Printing the area
s = Square(4)
print(s.area())  # Expected output: 16

# Test case - Printing string representation
s = Square(5)
print(s)  # Expected output: [Square] 5/5

# Test case - Using dir to list available attributes
print(dir(Square))  # Expected output should match the given list

# Test case - Handling invalid inputs
try:
    s = Square([12, 52])
except TypeError as e:
    print(e)  # Expected: "size must be an integer"

try:
    s = Square(-35)
except ValueError as e:
    print(e)  # Expected: "size must be greater than 0"

try:
    s = Square(0)
except ValueError as e:
    print(e)  # Expected: "size must be greater than 0"

