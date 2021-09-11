# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
import string

def is_pangram(s):
    for letter in string.ascii_lowercase:
        if letter not in s.lower():
            return False
    return True

