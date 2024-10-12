#commenting '#' 
'''hello everyone this is also 
commenting'''
#declare variable
a = 1 
#printing
print(a)

print(f'printing a {a} and its type {type(a)}')
#what if we change the type of a
a='hello' #becomes string
print(f'printing a {a} and its type {type(a)}')

''' Illegal variable : 
    2may = 2
    a-b = 3
    a b = 4'''

#----------------------------------- VARIABLE -----------------------------------------
# why not multiple variable
a,b,c=1,2,3
print(a,b,c)
ls = ['apple','banana','carrot']
a,b,c = ls
print(a,end=',')
print(b,',',c)   #techniques to print differently


#why not the we just take an output of the var ??

print(a+b+','+c) #string concatinate

# global variable
x=2
z=2
def func():
    y=3
    global z #To change the value of global var
    z=5
    print(f'global = {x} local or inside func() = {y} ')

func()
print(f'global = {x} local or inside func() cant be accessed BUT global z = {z} can be accessed ')
#during f'' use f" as can't ' may clash

x=4
def myfunc():
    x=5
    print(f'x = {x} takes the loacl one')

myfunc()
print(f'x = {x} takes the global one')

#----------------------------------- VARIABLE -----------------------------------------
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
#what about numbers ??
a=[1,1.23,1+2j]
for x in a:
    print(type(x))
#Lets print random from range 1 to 9
import random
print(random.randrange(1, 10))
#----------------------------------- CASTING -----------------------------------------

a=[1,1.23,'2']
#just found out u cant cast complex or 'hello' this str to int lol
for x in a:
    x=int(x)
    print(x,type(x))
