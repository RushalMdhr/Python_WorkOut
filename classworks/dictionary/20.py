# Write a Python program to find the specified number of maximum values in a given dictionary. 
# Original Dictionary: {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100} 
# 1 maximum value(s) in the said dictionary: ['f'] 
# 2 maximum value(s) in the said dictionary: ['f', 'i'] 
# 5 maximum value(s) in the said dictionary: ['f', 'i', 'g', 'd', 'c']
my_dict={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100} 
new=dict(sorted(my_dict.items(),key=lambda item:item[1],reverse=True))
keys = [k for k, v in new.items()]
print(keys[0:1])
print(keys[0:2])
print(keys[0:4])

    