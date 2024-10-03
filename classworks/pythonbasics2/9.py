''' 9. Write a Python script that takes two numbers as input and prints their sum, 
difference, product, and quotient using match case.'''

a=int(input("enter a"))
b=int(input("enter b"))
operation=(input("enter +,-,*,/"))
match operation:
    case "+":
        result = a + b
    case "-":
        result = a - b
    case "*":
        result = a*b
    case "/":
        result = a/b
    case _:
        result = "Unknown operation"

# Print the result
print(f"Result: {result}")



