'''1. Write a Python program to calculate the difference between a given number and 17. If the 
number is greater than 17, return twice the absolute difference.'''

n=int(input("enter the value of n"))

if n > 17 :
    print(2 * abs(n-17))
else:

    print(17-n)