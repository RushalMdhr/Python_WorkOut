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
n=int(input("enter number:"))
while n%10!=0:
    print(n)
    n=n//10