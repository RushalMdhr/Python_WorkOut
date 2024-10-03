'''14.Write a python program that takes a number and prints whether it is “Even”, “Odd”, “Zero”,or
“Invalid” for non-integer inputs. This program should first check if the input is a valid integer 
“Invalid” for non-integer inputs. This program should first check if the input is a valid integer 
and then check for the other conditions.'''

try:
    number = int(input("Enter a number: "))

    if number == 0:
        print("Zero")
    elif number % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid")
