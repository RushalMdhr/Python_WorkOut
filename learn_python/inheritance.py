class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(a):
        return f'my name is {a.fname}'

class student(person): #inheritance
    def __init__(self, fname, lname):
        self.fname = 'fname'
        self.lname = 'lname'
    pass

p = student('rushal','manandhar')
print(p)

#-----------------------------------------------lets only use parents
class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def __str__(a):
        return f'my name is {a.fname}'

class student(person): #inheritance
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname) #or this
        super().__init__(fname, lname)      #or this
        self.graduationyear = 2019
        print(self.graduationyear)
    pass

p = student('rushal','manandhar')
print(p)

class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

class student(person): #inheritance
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)      #or this
        self.graduationyear = year
        print(self.graduationyear)
    
    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

p = student('rushal','manandhar',2024)
p.welcome()
