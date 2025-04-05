#!/usr/bin/python3
"""A script that fetches https://intranet.hbtn.io/status with headers."""

if __name__ == '__main__':
    import urllib.request

    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    with urllib.request.urlopen(req) as resp:
        content = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
