#!/usr/bin/python3
number = 98
if not isinstance(number, int):
    raise ValueError("Unknown format code 'd' for object of type 'str'")

print(f"{number} Battery street")
