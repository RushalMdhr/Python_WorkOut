#print the following patterns
'''pattern1  pattern2   pattern3  pattern4  pattern5  pattern6  pattern7  pattern8  pattern9
   *****     *****          *     *****          *        *        *      1         10
   *****     ****          **      ****         **       * *      ***     23        98
   *****     ***          ***       ***        ***      * * *    *****    456       765
   *****     **          ****        **       ****                        78910     4321
   *****     *          *****         *      ***** 
                                              ****
                                               ***
                                                **
                                                 *                    

pattern10  pattern11  pattern12  pattern13  pattern14  pattern15  pattern16
   1          0          1       1          0          1 2        NEPAL
  121        101        123      01         11         2 3        NEPA
 12321      21012      12345     101        222        3 4        NEP
1234321               1234567    0101       3333       4 5        NE
                                 10101                 5 6        N
                                 010101
                                 1010101
                                 01010101
                                 101010101
                                 0101010101                               '''
#1
for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print()
print("SAME PATTERN DIFFERENT TECHNIQUES\n")
rows=5
for i in range(5):
    print('* ' * rows)

#2
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
#3
rows = 5
for i in range(rows):
    print('  ' * (rows - i-1) + '* ' * (i+1))
#4
rows = 5
for i in range(rows):
   print('  ' * i + '* ' * (rows-i))
#5
rows = 5

# Upper part of the pattern
for i in range(1, rows + 1):
    print('  ' * (rows - i) + '* ' * i)

# Lower part of the pattern
for i in range(rows - 1, 0, -1):
    print('  ' * (rows - i) + '* ' * i)
#6
rows = 3
for i in range(rows):
    print(' ' * (rows-i-1) + '* ' * (i+1))
#7
rows = 3
for i in range(1,rows+1):
    print('  ' * (rows-i) + '* ' * ((i*2)-1))
#8
rows = 4
num=1
for i in range(rows):
    for j in range(i+1):
        print(num,end=' ')
        num+=1
    print()
#9
rows = 4
num=10
for i in range(rows):
    for j in range(i+1):
        print(num,end=' ')
        num-=1
    print()
#10
rows=4

for i in range(rows):
    print('  ' * (rows-i-1),end=' ')
    for j in range(1,i+2):
        print(j,end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
#11
rows = 3

for i in range(rows):
    print('  ' * (rows - i - 1), end=' ')
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    # Print increasing numbers
    for j in range(i + 1):
        print(j, end=" ")
    
    print()
#12
rows=4

for i in range(1,rows+1):
    print('  ' * (rows-i),end=' ')
    for j in range(1,i*2):
        print(j,end=' ')
    print()
#13
rows = 10
for i in range(rows):
    for j in range(i+1):
        print(j%2,end=' ')
    print()
#14
rows = 4
for i in range(rows):
    for j in range(i+1):
        print(i,end=' ')
    print()
#15
rows = 5

for i in range(1,rows+1):
    print(f'{i} {i+1}')
    print()
#16
t = 'NEPAL'

for i in range(len(t),0,-1):
    print(t[:i])
