'''Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string : 'engineerings' 
Expected output: 'e': 3, 'n': 2, 'g': 2, 'i': 2, 'r': 1, 's': 1} '''
string ='engineerings'
l={char:string.count(char) for char in string}
print(l)
