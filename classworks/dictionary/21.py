# Write a Python program to find the key of the maximum and minimum values in a dictionary. 
# Original Dictionary: {'a': 5, 'b': 14, 'c': 32, 'd': 35} 
# Maximum and minimum key values: (‘d’, ‘a’)
my_dict= {'a': 5, 'b': 14, 'c': 32, 'd': 35}
max_key = max(my_dict, key=my_dict.get)
min_key = min(my_dict, key=my_dict.get)
print('Maximum key:', max_key)
print('Minimum key:', min_key)