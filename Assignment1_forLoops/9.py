rows = 4
num=10
for i in range(rows):
    for j in range(i+1):
        print(num,end=' ')
        num-=1
    print()