# 14. Write a Python function that takes a string as input and counts the number of uppercase and lowercase
# characters in the string. 
def count_char(string):
    ucount = 0
    lcount = 0
    for char in string:
        if char.isupper(): 
            ucount += 1
        elif char.islower():
            lcount += 1
    return ucount, lcount
string = "Hello World!"
ucase, lcase = count_char(string)
print(f"Uppercase: {ucase}")
print(f"Lowercase: {lcase}")