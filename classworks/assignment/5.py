'''5. WAP to enter a number from user and print sum of its individual digits 
153 --> 9'''
n=int(input('enter a number : '))
s=0
while n%10!=0: #0
    s+=(n%10) #8+1=9
    n=(n//10)
print(s)