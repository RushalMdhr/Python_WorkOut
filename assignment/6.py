'''6. WAP to enter a number from user and check if it is pallindrome or not 
121 - 121 
12321 - 12321 '''
num = input("Enter a number: ")
if num == num[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
