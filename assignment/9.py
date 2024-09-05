'''9. WAP to enter a limit from user and print fibonacii series 
0 1 1 2 3 5 8 13 '''
n= int(input("Enter the limit for the Fibonacci series: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    c=a+b
    a, b = b, c
print()
