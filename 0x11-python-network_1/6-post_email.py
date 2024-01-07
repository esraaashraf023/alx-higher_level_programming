#!/usr/bin/python3
"""This IS script sends a POST request to a URL.."""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    response = requests.post(url, data=data)

    print(response.text)
