#sort by itself
#double values are written in single

a={1,1,2,3,True}
print(a) # true =1 
print(list(a))
print(tuple(a))
print(set(list(a)))

#----------------------------------ADDING ITEMS-------------------------

a.add('nine')
print(a)
b=[1,2,3,4,5]
a.update(b)
print(a)
a.update('hello')
print(a)

#----------------------------------REMOVE ITEMS-------------------------
# remove or discard or pop
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

a={1,2,3,4}
b={2,3,4,5}
c={'red','white'}
print(a.union(b,c))
print(a|b|c)

