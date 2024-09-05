for i in range(5):
    for j in range(i,5):
        print("*",end=" ")
    print()

print("SAME PATTERN DIFFERENT TECHNIQUES\n")

rows = 5
for i in range(5):
    print('* '* (rows-i))

print("SAME PATTERN DIFFERENT TECHNIQUES\n")

for i in range(rows, 0, -1):
    print('* ' * i)
