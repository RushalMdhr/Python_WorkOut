#Write a python script to check whether the key ‘email’ exists in the dictionary. If it does not exist 
#print ‘key not found’. 
person = {'name': 'Hari', 'age': '29', 'city': 'Bhaktapur'}
# Checking if 'email' exists
if 'email' in person:
    print(person['email'])
else:
    print('key not found')
