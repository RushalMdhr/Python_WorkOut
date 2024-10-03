'''12. Create a program that asks for an age and prints “Child” 
if the age is less than 12, “Teenager” if the age is between 13 and 19, 
and “Adult” for ages 20 and above'''

age = int(input("Enter your age: "))

if age < 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")
