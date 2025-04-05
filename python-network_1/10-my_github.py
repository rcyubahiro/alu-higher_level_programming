#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's ID.
"""
import sys
import requests

if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print(None)
