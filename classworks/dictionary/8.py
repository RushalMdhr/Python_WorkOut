'''Write a Python script to merge two Python dictionaries. 
dict1 = {'a': 1, 'b': 2} and dict2 = {'b': 3, 'c':4} merge them into a single dictionary. 
What happens to the value of the key 'b'? '''
dict1 = {'a': 1, 'b': 2} 
dict2 = {'b': 3, 'c':4}
merged_dict={**dict1,**dict2}
print(merged_dict)
