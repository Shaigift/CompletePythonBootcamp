#Write a Python function that checks whether a word or phrase is palindrome or not

def palindrome(s):
    return s == s[::-1]

s = "eve"
ans = palindrome(s)

if ans:
    print("Yes")
else:
    print("No")

