'''3. WAP to print following series 
a.1 4 9 16 25 36 49 64 81 100 
b.1/1 2/4 3/9 4/16 5/25 6/36 7/49 8/64 9/81 10/100 
c.1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10'''
# a. Square numbers from 1 to 100
for i in range(1, 11):
    print(i**2, end=" ")
print()

# b. Fraction series 1/1 2/4 ... 10/100
for i in range(1, 11):
    print(f"{i}/{i**2}", end=" ")
print()

# c. Sum of numbers from 1 to 10
for i in range(1, 11):
    print(i,"+",end=" ")
