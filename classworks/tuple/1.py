#1. Write a Python program to convert a tuple to a string. 
my_tuple = ('apple', 'banana', 'cherry')
tuple_as_string = ' '
for item in my_tuple:
    tuple_as_string += item

print(tuple_as_string,end="  ")