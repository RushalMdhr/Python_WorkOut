# #######        LAB 2
#         # Python Basics 2
# # 1. Write a Python program to calculate the difference between a given number and 17. If the
# # number is greater than 17, return twice the absolute difference. 
# # 
# num=int(input("Enter the number: "))
# if num>17:
#     print(2*(num-17))
# else:
#     print(num-17)

# # 2. Write a Python program that determines whether a given number (accepted from the user) is
# # even or odd, and prints an appropriate message to the user. 
# num=int(input("Enter the number: "))
# if num%2==0:
#     print(f'given number {num} is even')
# else:
#     print(f'given number {num} is odd')

# # 3. Write a Python program to count the number 4 in a given list. 
# lst=[1,3,4,5,4,8]
# count = lst.count(4)

# print('Count of 4:', count)
# # 4. Write a Python program to swap two variables. 
# x,y=2,3
# print(x,y)
# y,x=x,y
# print(x,y)

# # 5. Write a Python program to check whether a variable is an integer, or string, or a list, or tuple, or
# # set.
# lst=['hello','bye','now']
# print(type(lst))

# # 6. Write a Python script that takes two numbers as input and prints their sum, difference, product,
# # and quotient.
# print(x+y)
# print(x-y)
# print(x*y)
# print(x%y)
# # 7. Take an input from user then reverse the string using slicing.

# word = 'NEPAL'
# print(word)
# print(word[::-1])
# # 8. Write code to take input from user and store it in a variable spam then print Hello if 1 is stored
# # in spam, print Hi if 2 is stored in spam, and print Greetings! if anything else is stored in spam. 
# choice = int(input("enter choice 1/2/... : "))
# match(choice):
#     case 1:
#         print("HELLO")
#     case 2:
#         print("HI")
#     case _:
#         print("greatings")
# # 9. Write a Python script that takes two numbers as input and prints their sum, difference, product,
# # and quotient using match case.
# choice = input("operator :")
# match(choice):
#     case '+':
#         print(x+y)
#     case '-':
#         print(x-y)
#     case '*':
#         print(x*y)
#     case '%':
#         print(x%2)


# # 10. Write a script that asks the user for their name and age, then prints a message that tells them the
# # year in which they will turn 100 years old.
# name,age = input("enter your name : "),int(input("enter your age : "))
# print(f'you will turn 100 years {2081+(100-age)}')
# 11. Create a Python script that converts temperature from Fahrenheit to Celsius and vice versa, based
# on user input
# temp = int(input("current temp : "))
# choice = input("convert to 1.Fahrenheit / 2.Celsius : ")
# match(choice):
#     case '1':
#         print(f'Fahrenheit : {(temp * 9/5) + 32}')
#     case '2':
#         print(f'celsius : {(temp-32)*(5/9)}')

# 12. Create a program that asks for an age and prints “Child” if the age is less than 12, “Teenager” if
# the age is between 13 and 19, and “Adult” for ages 20 and above
# age=int(input("enter your age : "))
# match(age):
#     case age if age<12:
#         print(f"child")
#     case age if age>=13 and age <=19:
#         print(f"teenager")
#     case age if age>=20:
#         print(f"adult")
# 13. Write a python script that takes a letter grade (A, B, C, D, F) as input and prints the
# corresponding grade point average (GPA). For example, A = 4.0, B = 3.0, C = 2.0, D = 1.0,
# F=0.0. Include an else statement to handle invalid inputs.
grade = input("GRADES : ").upper()
match(grade):
    case 'A':
        print("4.0")
    case 'B':
        print("3.0")
    case 'C':
        print("2.0")
    case 'D':
        print("1.0")
    case 'F':
        print("FAIL!")
    case _:
        print("Invalid Grade")

# 14. Write a python program that takes a number and prints whether it is “Even”, “Odd”, “Zero”, or
# “Invalid” for non-integer inputs. This program should first check if the input is a valid integer
# and then check for the other conditions.
# def check_number(value):
#     try:
#         num = int(value)
#         if num == 0:
#             print("Zero")
#         elif num % 2 == 0:
#             print("Even")
#         else:
#             print("Odd")
#     except ValueError:
#         print("Invalid")

# # Take input from the user
# user_input = input("Enter a number: ")
# check_number(user_input)


# 15. An extra day is added to the calendar almost every four years as February 29, and the day is
# called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25
# days to orbit the sun. A leap year contains a leap day.
# In the Gregorian calendar, three conditions are used to identify leap years:
#           • The year can be evenly divided by 4, is a leap year, unless: 
#           • The year can be evenly divided by 100, it is not a leap year, unless: 
#           • The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800,
# 1900, 2100, 2200, 2300 and 2500 are not leap years.
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True
# otherwise return False.


