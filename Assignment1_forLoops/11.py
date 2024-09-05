rows = 3

for i in range(rows):
    print('  ' * (rows - i - 1), end=' ')
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    # Print increasing numbers
    for j in range(i + 1):
        print(j, end=" ")
    
    print()
