#!/usr/bin/python3
"""
Script that fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == '__main__':
    url = "https://intranet.hbtn.io/status"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    text = r.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
