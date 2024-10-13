# The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# The function will print the local x, and then the code will print the global x:

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)

# If you use the nonlocal keyword, the variable will belong to the outer function:

def myfunc1():
  x = "1"
  def myfunc2():
    # nonlocal x
    x = "2"
    def myfunc3():
        nonlocal x
        x = "3"
    myfunc3()
    print(x)
  myfunc2()
  return x

print(myfunc1())