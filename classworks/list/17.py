#17. Write a Python Program to sort a list of lists by a given index of the inner list. 
list=[[1,2],[5,6],[3,4]]
list.sort(key=lambda x:x[-1])
print(list)
