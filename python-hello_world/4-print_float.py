#!/usr/bin/python3
number = 3.14159

if not isinstance(number, (int, float)):
    raise ValueError("Unknown format code 'f' for object of type 'str'")

print(f"Float: {number:.2f}")
