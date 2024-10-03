#3. Write a Python program to find repeated items in a tuple. 
tup=(1,1,2,3,4,5,6)
repeated=set([x for x in tup if tup.count(x)>1])
print(repeated)