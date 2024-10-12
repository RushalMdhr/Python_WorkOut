a= [1,'hello',2.3,'no',6]
print(a)
print(len(a))
print(type(a))
#access same as string 
print(a[1:3])
for x in a:
    print(x)
if 'no' in a:
    print('why not')

#changing the list item
print(a[2])
a[2]=33
print(a[2])
a.append('yes')
print(a)
a.insert(4,'why not')
print(a)
a=['apple','banana','cherry']
b=[1,2,3,4,5]
print(a)
a.extend(b)
print(a)
a.remove(4)
print(a)
a.pop(1)
print(a)
del a[1]
print(a)
del a
print(a)