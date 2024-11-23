# 11. Write a function that takes a list of numbers and print each number doubled. 

newlist=[]
def double(lst):
   for x in lst:
       newlist.append(x*2)
       print(x*2)

lst = [1,2,3,4]
double(lst)
print(newlist)