#!/usr/bin/python3
"""sends a request to the URL and displays the body"""
import sys
import requests as rq


if __name__ == "__main__":
    req_ = rq.get(sys.argv[1])
    if req_.status_code >= 400:
        print('Error code: {}'.format(req_.status_code))
    else:
        print(req_.text)
