a=(1,2,3)
print(type(a))
a=(2) #is not a tuple 
print(type(a))

# its same as list but cant be modified like a turtle shell ()
a=tuple(str(123))
print(a)

#------------------------------------UNPACK TUPLE ---------------------------------------

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry")
x,y,z = fruits
print(x)
print(y)
print(z)

fruits = ("apple", "banana", "cherry",'brain')
x,*y,z= fruits
print(x)
print(y) #baki ko yeslaai dine kaile kai badi huda
print(z)

#------------------------------------JOIN TUPLES ---------------------------------------
# fruits *2 or fruits +fruits

print(fruits *2)
print(fruits + fruits)

