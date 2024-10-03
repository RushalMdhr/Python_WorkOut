'''5. Write a Python program to check whether a variable is an integer, 
or string, or a list, or tuple, or set.'''

var=[2]
if isinstance(var,int):
  print("integer")
elif isinstance(var,str):
  print("string")
elif isinstance(var,list):
  print("list")
elif isinstance(var,set):
  print("set")
elif isinstance(var,tuple):
  print("tuple")
  

