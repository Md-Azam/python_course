# import math
# from math import ceil


def palindrome_string(s):
    if s == s[::-1]:
        print(f"your string is palindrome- {s}")
    else:
        print("sorry your string not a palindrome ")

