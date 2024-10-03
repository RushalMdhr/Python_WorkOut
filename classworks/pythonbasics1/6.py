#6. Write a Python program to check whether a variable is an integer or string or float.
x="malika"
#x =(input("enter number 1"))
if isinstance(x, int):
    print("Integer")
elif isinstance(x, str):
    print("String")
elif isinstance(x, float):
    print("Float")