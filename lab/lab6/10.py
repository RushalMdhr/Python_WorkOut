# 10. Create a function that takes a list and a number, return a list after adding the number to the list preventing
# it from changing the original list. 
def add_to_list(original_list, number):
    new_list = original_list[:]
    new_list.append(number)

    return new_list

lst=[1,2,3,4]
new_list = add_to_list(lst,33)
print(f'old list:{lst} \n new list {new_list}')