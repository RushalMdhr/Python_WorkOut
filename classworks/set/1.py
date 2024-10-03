'''12. Write a Python program to create an intersection, a union, set difference and a symmetric 
difference of sets. Also find the length, maximum and minimum values in a set.'''
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1 & set2
union = set1 | set2
difference = set1 - set2
symmetric_difference = set1 ^ set2
length_of_set1 = len(set1)
max_value_set1 = max(set1)
min_value_set1 = min(set1)
print("Set 1:", set1)
print("Set 2:", set2)
print("Intersection of set1 and set2:", intersection)
print("Union of set1 and set2:", union)
print("Difference (set1 - set2):", difference)
print("Symmetric difference (set1 ^ set2):", symmetric_difference)
print("Length of set1:", length_of_set1)
print("Maximum value in set1:", max_value_set1)
print("Minimum value in set1:", min_value_set1)