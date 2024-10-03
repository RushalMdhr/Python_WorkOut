#3. Write a Python Program to get the largest and smallest number in a list without using built
#in functions. 
my_list=[1,4,6,7,8,2]
smallest=my_list[0]
largest=my_list[0]
for num in my_list:
    if num<smallest:
        smallest=num
    elif num>largest:
        largest=num
print(smallest)
print(largest)