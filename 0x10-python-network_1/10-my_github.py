#!/usr/bin/python3
"""my github"""


import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = str(sys.argv[1])
    passw = sys.argv[2]
    req = requests.get(url, auth=(user, passw))
    print(req.json().get('id'))
