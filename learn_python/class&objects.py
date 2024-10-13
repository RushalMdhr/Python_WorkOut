class hello:
    pass

object#object = person() #constructor

#-----------------------------------init function 
class person:
    def __init__(self,name,age): #built in function
        print('hello world')
        self.name = name
        print(name)
        print(self.name)
        self.age=age

p2 = person('name',30)

print(p2.name)
print(p2.age)

# -------------------------------------------------__str__() Function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
     return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)   #to show the object or self values
# del p1.age
# print(p1)

#----------------------------------------------object method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#-----------------------------------------instead of self
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()