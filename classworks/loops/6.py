import random

target = random.randint(1, 9)
guess = int(input("Enter the number: "))
print(target)
if guess == target:
    print("You won!")
else:
    print("Try again!")

