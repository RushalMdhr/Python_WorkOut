'''8. WAP to enter a number from user and print factorial of it 
5! -- 5*4*3*2*1 --> 120'''
n=int(input("enter number:"))
fact=1
while n!=0:
    print(f'{n}',end=" ")
    if n!=1:
        print("*",end=" ")
    fact*=n
    n=n-1
print("=",fact)