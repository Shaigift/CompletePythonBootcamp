#write a function that accepts a string and calculates the number of upper case letters and lower case letters

def up_low(s):
    d= {'upper':0, 'lower':0}

    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            pass

    print(f"Original String: {s}")
    print(f"Lowercase count: {lowercase}")
    print(f"Uppercase count: {uppercase}")


