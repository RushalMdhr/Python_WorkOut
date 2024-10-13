#we all know function 
def myfunc(name): #before any function we need to call and the create the funtion
    print(name)

myfunc('''input('name : ')''' 'rushal')
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#------------------------------------- Arbitrary Arguments, *args
def a(*numbers): #as a tuple basdo reixa
    print(type(numbers))

a('1','2','3')

#------------------------------------- Keyword Arguments
def many(a1,a2,a3):
  print(f'a1={a1},a2={a2},a3={a3}')

many(a1=1,a3=3,a2=2)

# --------------------------- Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"]) 

my_function(fname = "Tobias", lname = "Refsnes")

# Default Parameter Value
def okay(a=3):
  return a

print(okay(2))
print(okay())

# ombine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
# To specify that a function can have only positional arguments, add , / after the arguments:
# To specify that a function can have only keyword arguments, add *, before the argu