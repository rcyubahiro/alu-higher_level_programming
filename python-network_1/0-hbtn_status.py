#!/usr/bin/python3
"""
Script that fetches https://alu-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == '__main__':
    url = "https://alu-intranet.hbtn.io/status"
    
    # Using with statement to open the URL
    with urllib.request.urlopen(url) as response:
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
