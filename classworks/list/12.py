# 12. Write a Python Program to merge two lists and removes all duplicates from the combined 
# list.
list1=[1,2,2,3,9]
list2=[3,4,6,8,8]
new=list(set(list1+list2))
print(new)