'''13. Write a python script that takes a letter grade (A, B, C, D, F) as input and prints the 
corresponding grade point average (GPA). For example, A = 4.0, B = 3.0, C = 2.0, D = 1.0, 
F=0.0. Include an else statement to handle invalid inputs.'''

grade = input("Enter your letter grade (A, B, C, D, F): ").upper()

if grade == "A":
    print("GPA: 4.0")
elif grade == "B":
    print("GPA: 3.0")
elif grade == "C":
    print("GPA: 2.0")
elif grade == "D":
    print("GPA: 1.0")
elif grade == "F":
    print("GPA: 0.0")
else:
    print("Invalid grade")
