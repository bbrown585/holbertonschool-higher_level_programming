#!/usr/bin/python3
"""request to the URL and displays the body of the \
    response (decoded in utf-8)."""
import sys
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as f:
            print(f.read().decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
