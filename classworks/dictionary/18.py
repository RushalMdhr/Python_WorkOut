#Write a Python program to find the highest 3 values of corresponding keys in a dictionary. 
z={'e': 3, 'n': 2, 'g': 2, 'i': 2, 'r': 1, 's': 1}
new=sorted(z.values(),reverse=True)[:3]
print(new)
