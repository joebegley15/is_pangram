import string

def is_pangram(s):
    alphabet = string.ascii_lowercase
    s = s.lower()
    for letter in alphabet:
        if letter not in s:
            return False
    return True