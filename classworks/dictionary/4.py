#Write a Python program to remove a key ‘age’ from the dictionary. 
# Removing the key 'age'
person = {'name': 'Hari', 'age': '29', 'city': 'Bhaktapur'}
person.pop('age', None)
print(person)
