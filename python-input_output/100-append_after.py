#!/usr/bin/python3
"""Function that inserts line of text to file containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Search and update the file content."""
    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
