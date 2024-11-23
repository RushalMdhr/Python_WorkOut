# 12. Defines a function called calculate_average that takes a list of numbers as input and calculate the
# average of list. Finally, the function returns the average of that list. 

import numpy

def calculate(list):
   print(numpy.average(list))
   avg=0
   for x in list:
       avg+=x
   print(avg/len(list))

list=[1,2,3,4,5,6]
calculate(list)