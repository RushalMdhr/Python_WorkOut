# lambda arguments : expression

x = lambda a : a + 10
print(x(5)) #it calls x as an function 

# x=5 and {a=5; return a+10}

x = lambda a, b,c : a+b+c
print(x(5, 6,7))

# Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
# mytripler = myfunc(3)

print(mydoubler(11))
print(mydoubler(2))