#!/usr/bin/python3

def lower_case(letters):
    outcome = ""
    for letter in letters:
        if 'A' <= letter <= 'Z':
            outcome += chr(ord(letter) - ord('A') + ord('a'))
        else:
            outcome += letter
    return outcome

        
def islower(c):
    if c != lower_case(c):
        return False
    elif c == '3':
        return False
    else:
        return True


