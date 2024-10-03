'''10. WAP to print following patterns 
a.    b.       c.     d.      e.     f.     g.      h.     i.     j.      k. 
*      *****   1      1       5      5      55555   54321  12345  11111   1 
**     *****   12     22      44     54     4444    5432   1234   2222    23 
***    *****   123    333     333    543    333     543    123    333     456 
****   *****   1234   4444    2222   5432   22      54     12     44      78910 
*****  *****   12345  55555   11111  54321  1       5      1      5             '''

#a
for i in range(1, 6):
    print('*' * i)
print()

#b
for i in range(5):
    print('*****')

#c
rows=5
for i in range(rows):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
#d
rows = 4
for i in range(rows+1):
    for j in range(i+1):
        print(i+1,end=' ')
    print()

#e
rows=5
num=rows
for i in range(rows+1):
    for j in range(rows,rows-i,-1):
        print(num+1,end=' ')
    num-=1
    print()
#f
rows=5

for i in range(rows):
    for j in range(rows,rows-i-1,-1):
        print(j,end=' ')
    print()

#g
rows=5
num=rows
for i in range(rows):
    for j in range(rows-i):
        print(num,end=' ')
    print()
    num-=1

#h
rows=5
for i in range(rows):
    for j in range(rows,i,-1):
        print(j,end=' ')
    print()

#i
rows=5
for i in range(rows):
    for j in range(i+1,rows+1):
        print(j,end=' ')
    print()

#j
rows=5
num=1
for i in range(rows):
    for j in range(rows-i):
        print(num,end=' ')
    print()
    num+=1

#k
rows = 4
num=1
for i in range(rows):
    for j in range(i+1):
        print(num,end=' ')
        num+=1
    print()