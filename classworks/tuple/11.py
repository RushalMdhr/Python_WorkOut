'''11. Write a Python program to compute the sum of all the elements of each tuple stored inside a 
list of tuples. 
Original list of tuples: 
[(1, 2), (2, 3), (3, 4)] 
Sum of all the elements of each tuple stored inside the said list of tuples: 
[3, 5, 7] 
Original list of tuples: 
[(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)] 
Sum of all the elements of each tuple stored inside the said list of tuples: 
[9, -1, 7, 8]'''
list_of_tuples = [(1, 2), (2, 3), (3, 4)]
sum_of_elements = [sum(tpl) for tpl in list_of_tuples]
print("Sum of all the elements:")
print(sum_of_elements)