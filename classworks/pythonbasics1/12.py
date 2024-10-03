'''12. Write a Python program to calculate the sum of three given numbers. 
If the values are equal, returs three times their sum''' 

a, b, c = 5, 5, 5
if a == b == c:
    print(3 * (a + b + c))
else:
    print(a + b + c)
