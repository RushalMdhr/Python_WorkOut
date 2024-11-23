# 15. Write a Python recursive function to find out factorial of any given number. 
n=int(input("enter the value of n"))
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
result=fact(n)
print("fact:",result)