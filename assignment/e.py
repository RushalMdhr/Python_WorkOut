rows=5
num=rows
for i in range(rows):
    for j in range(rows,rows-i,-1):
        print(num,end=' ')
    num-=1
    print()