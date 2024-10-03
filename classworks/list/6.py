#6. Write a Python program to multiply all the items in a list.
my_list=[1,2,3,4,5]
total_mul=1
for items in my_list:
    total_mul*=items
print(total_mul,end="")