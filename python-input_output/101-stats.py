#!/usr/bin/python3
"""
Script that reads from standard input and computes metrics:
- Prints total file size after every 10 lines and at the end.
- Prints the count of specific status codes encountered.
"""

import sys


def print_status(size, status_codes):
    """Prints the file size and status code counts."""
    print("File size: {}".format(size))
    for key, val in sorted(status_codes.items()):
        if val > 0:
            print("{}: {}".format(key, val))


def process_logs():
    """Reads input line by line and computes metrics."""
    counter = 0
    size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            parts = line.strip().split()

            if len(parts) < 2:
                continue  # Skip malformed lines

            try:
                file_size = int(parts[-1])
                status_code = parts[-2]

                size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                continue  # Skip lines with invalid numbers

            counter += 1
            if counter == 10:
                print_status(size, status_codes)
                counter = 0

    except KeyboardInterrupt:
        print_status(size, status_codes)
        raise

    print_status(size, status_codes)


if __name__ == "__main__":
    process_logs()
