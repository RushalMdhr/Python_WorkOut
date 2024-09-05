rows=5
num=1
for i in range(rows):
    for j in range(rows-i):
        print(num,end=' ')
    print()
    num+=1