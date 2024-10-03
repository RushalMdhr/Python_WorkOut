#Use the get() method to fetch the value of ‘age’ from the above dictionary. If the ‘age’ is not a key, 
#it should return ‘Key not available’. 
person = {'name': 'Hari', 'age': '29', 'city': 'Bhaktapur'}
value=person.get('age','key not available')
print(value)