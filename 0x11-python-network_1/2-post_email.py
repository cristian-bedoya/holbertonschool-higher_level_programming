#!/usr/bin/python3
""" Write a Python script that takes in a URL and an email
sends a POST request to the passed URL"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    body = data.encode('ascii')
    req = urllib.request.Request(url, body)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
