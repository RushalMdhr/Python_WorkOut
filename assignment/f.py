rows=5

for i in range(rows):
    for j in range(rows,rows-i-1,-1):
        print(j,end=' ')
    print()