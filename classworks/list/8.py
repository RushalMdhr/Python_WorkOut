#8. Write a Python program to print the numbers of a specified list after removing even 
#numbers from it.
list=[1,2,3,4,5,6]
new_list=[]
for i in list:
    if i%2!=0:
        new_list.append(i)
print(new_list)
