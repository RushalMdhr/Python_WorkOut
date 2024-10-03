# Write a Python program to drop empty items from a given dictionary. 
#Original Dictionary: {'c1': 'Red', 'c2': 'Green', 'c3': None} 
#New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}
Original_Dictionary={'c1': 'Red', 'c2': 'Green', 'c3': None} 
cleaned_dict = {k: v for k, v in Original_Dictionary.items() if v is not None}
print(cleaned_dict)

