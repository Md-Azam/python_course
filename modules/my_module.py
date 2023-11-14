from math import *
import math


print(ceil(2.7))

def isPlaindrome(s):
    s_reverse =  ''
    if s_reverse == s[::-1]:
        print(f'string is palindrome {s} == {s_reverse}')
    else:
        print("string is not palindrome")


