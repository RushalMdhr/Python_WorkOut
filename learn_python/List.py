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

#------------------------------------CHANGE ITEM---------------------------------------
print(a[2])
a[2]=33
print(a[2])
#------------------------------------ADD ITEM---------------------------------------
a.append('yes')
print(a)
a.insert(4,'why not')
print(a)
a=['apple','banana','cherry']
b=[1,2,3,4,5]
print(a)
a.extend(b)
print(a)
#------------------------------------REMOVE ITEM---------------------------------------
a.remove(4)
print(a)
a.pop(1)
print(a)
del a[1]
print(a)
# del a
# print(a)
#------------------------------------LOOP LIST---------------------------------------
for x in a:
    print(x)
for i in range(len(a)):
    print(a[i])

#------------------------------------COMPARE IN LIST---------------------------------------
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
# newlist = [expression for item in iterable if condition == True
print(newlist)

del newlist
newlist = [fruits[x] for x in range(3)]
print(newlist)

del newlist
newlist = [x.upper() for x in fruits]
print(newlist)

# these all arae kind of lamda function 
# if we want to add if else then we need to add before for x in 
a=[5,3,4,1,2]
b=[x if x!=3 else 'its three' for x in a]
print(b)

#------------------------------------SORT THE LIST---------------------------------------
a.sort()
print(a)
b.append('its two')
print(b)
# b.sort()  cant be sort with str and int but we can by
# print(b)
b=list(set(b))  #though it doesnt sort the str but only int
print(b)
a.sort(reverse = True)
print(a)
# Sort the list based on how close the number is to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


# to create case in sensetive sort
thislist = ["banana", "Orange", "kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
thislist.reverse()
print(thislist)

#------------------------------------COPY LIST---------------------------------------

a= thislist.copy()
print(f'a = {a}')
del a
a=thislist  #this points to same memory address but we need to copy so not this one
print(f'a = {a}')
a=thislist[:]       #any of these
a=list(thislist)    #any of these

#------------------------------------JOIN LIST ---------------------------------------
a=[1,2,3,4]
b=['one ','two','three','four']
print(a+b)
for x in b:
    a.append(x)
print(a)