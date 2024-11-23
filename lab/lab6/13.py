# 13. Write a Python function that checks whether a passed string is a palindrome or not. 
def check(a):
    for i in range(len(a)//2):
        if a[i] != a[-(i+1)]:
            print('not palindrome')
            return 1
    print('palindrome')
a='2abcba2'
check(a)