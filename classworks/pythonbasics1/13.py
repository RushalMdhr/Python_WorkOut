'''13. Write a Python program to sum two given integers. 
However, if the sum is between 15 and 20 it will return 20.'''

a, b = 10, 6
sum= a + b
if 15 <= sum<= 20:
    print(20)
else:
    print(sum)
