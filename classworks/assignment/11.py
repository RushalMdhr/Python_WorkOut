'''print the following:
a.  *   b.  *      c.  *       
   **      ***        ***
  ***     *****      *****
 ****    *******    *******
*****   *********  *********                  
                    *******
                     *****
                      ***
                       * '''

#a
rows = 5
for i in range(rows):
    print('* ' * (i+1))

#b
rows=5
for i in range(1,rows+1):
    print(' '*(rows-i) + '*' * (2*i-1),end='')
    print()

#c
rows=5
for i in range(1,rows+1):
    print(' '*(rows-i) + '*' * (2*i-1),end='')
    print()

for i in range(rows - 1, 0, -1):
    print(' '*(rows-i) + '*' * (2*i-1),end='')
    print()
