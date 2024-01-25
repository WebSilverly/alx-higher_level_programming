#!/usr/bin/python3
"""def islower(c):
    if c == c.upper():
        return False
    else:
        return True"""

"""def islower(c):
    if ord(c) % 2 == 0:
        return False
    else:
        return True"""

def under(m):
    outcome = ""
    for letters in m:
        if 'A' <= letters <= 'Z':
            outcome += chr(ord(letters) - ord('A') + ord('a'))
        else:
            outcome += letters
    return outcome


def islower(c):
    if c != under(c):
        return False
    else:
        return True
