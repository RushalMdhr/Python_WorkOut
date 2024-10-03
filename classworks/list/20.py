# 20. Write a  Python program to insert n values in a list and find those values in a list that are 
# greater than a specified number.
list=list(map(int,input("enter the numbers").split()))
s=int(input("enter specified number"))

new_list=[]
for i in list:
    if i>s:
        new_list.append(i)
print(new_list)
