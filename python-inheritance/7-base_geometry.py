#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

# Test valid cases
bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

# Test invalid cases
try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 13.5)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test the area method
try:
    bg.area()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
