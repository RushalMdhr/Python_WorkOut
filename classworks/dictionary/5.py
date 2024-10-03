#Write a python program to loop to iterate through the dictionary from the first question and print all keys and their corresponding values.
person = {'name': 'Hari', 'age': '29', 'city': 'Bhaktapur'}
for key, value in person.items():
    print(f"{key}: {value}")
