#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
body of the response using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL, sends a request to the URL and displays the
    body of the response using requests
    """
    url = argv[1]
    rqst = requests.get(url)
    if rqst.status_code >= 400:
        print("Error code: {}".format(rqst.status_code))
    else:
        print(rqst.text)
