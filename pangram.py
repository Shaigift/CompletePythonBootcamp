#Write a Python function to check whether a string is pangram or not

import string


def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True


# Driver code
string = 'tcecececps overeefascdac the lazycdceceg'
if (ispangram(string) == True):
    print("Yes")
else:
    print("No")
