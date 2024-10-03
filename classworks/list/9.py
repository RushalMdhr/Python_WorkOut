# 9. Write a Python Program to print a specified list after removing the 0th, 4th and 5th element. 
# Sample list: [‘Red’, ‘Green’, ‘White’, ‘Black’, ‘Pink’, ‘Yellow’] 
# Expected Output: [‘Green’, ‘White’, ‘Black’]
list=['red','green','white','black','pink','yellow']
new=[list[i] for i in range(len(list)) if i not in [0,4,5]] 
print(new)
    

