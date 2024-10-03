n= int(input("Enter the limit for the Fibonacci series: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    c=a+b
    a, b = b, c
print()