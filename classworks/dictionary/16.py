'''Given a dictionary d = {'a':1, b':2, 'c':3}, write a python script to reverse the key-value pairs to 
get a new dictionary. '''
d ={'a':1,'b':2,'c':3}
new={value:key for key,value in d.items()}
print(new)