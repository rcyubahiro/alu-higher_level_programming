#!/usr/bin/python3
"""
Script that fetches http://0.0.0.0:5050/status
"""
import requests

if __name__ == '__main__':
    url = "http://0.0.0.0:5050/status"  # Change the URL to the required one
    response = requests.get(url)
    text = response.text

    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
