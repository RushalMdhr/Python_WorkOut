rows=4

for i in range(1,rows+1):
    print('  ' * (rows-i),end=' ')
    for j in range(1,i*2):
        print(j,end=' ')
    print()