#7. Write a Python program to test if a variable is a list, tuple, or set.
x = (1, 2, 3) 
if isinstance(x, list):
    print("List")
elif isinstance(x, tuple):
    print("Tuple")
elif isinstance(x, set):
    print("Set")
