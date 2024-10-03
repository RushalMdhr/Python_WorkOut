#Write a Python program to sort a dictionary by values instead of keys. 
dict1={1:2,3:1,2:3}
new=dict(sorted(dict1.items(),key=lambda item:item[1]))
print(new)