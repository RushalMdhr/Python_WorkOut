# 10. Write a Python Program to check if each number is prime in a given list of numbers. Print 
# the prime numbers if any, otherwise print “no prime numbers”.
list=[2,3,5,7,11,12]
chk=0
r=0
for i in range (0,len(list)):
    a=2
    while(a!=list[i]):
        if(list[i]%a==0):
            r+=1
        a+=1
    if r==0:
        print(list[i])
        chk+=1
if (chk==0):
    print("no prime numbers")
