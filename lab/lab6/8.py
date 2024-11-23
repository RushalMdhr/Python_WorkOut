# 8. Write a Python function to find the maximum and minimum value, sum and multiplication of all the
# numbers in a list. 
import math
def find(lst):
    print(max(lst),min(lst),sum(lst),math.prod(lst))

lst = [2,3,1,5,6,9,8]
find(lst)