'''9. Write a Python program to convert a given tuple of positive integers into an integer. 
Original tuple: 
(1, 2, 3) 
Convert the said tuple of positive integers into an integer: 
123 
Original tuple: 
(10, 20, 40, 5, 70) 
Convert the said tuple of positive integers into an integer: 
102040570 '''
tuple_of_integers = (1, 2, 3)
integer_as_string = ''.join(map(str, tuple_of_integers))
integer_value = int(integer_as_string)
print("Converted set of tuple of positive integers into an integer:")
print(integer_value)