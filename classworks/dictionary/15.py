'''Write a Python program to sort a list alphabetically in a dictionary. 
Sample: num_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]} 
Output: {'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]} '''
sample=num_dict = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for key,value in num_dict.items():
    num_dict[key]=sorted(value)
print(num_dict)
