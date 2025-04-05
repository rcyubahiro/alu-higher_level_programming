#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
from sys import argv

if __name__ == '__main__':
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    
    # If the response was unsuccessful, return None
    if r.status_code != 200 or not r.text.strip():
        print(None)
    else:
        print(r.text)
