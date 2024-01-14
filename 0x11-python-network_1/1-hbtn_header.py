#!/usr/bin/python3
"""
A script that takes an url and sends the request_id
"""

import sys
import urllib.request

if __name__ == "__main__":
  url = sys.argv[1]
  
  request = urllib.request.Request(url)
  with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))