# 9. Write a python program to demonstrate positional argument and functional arguments in function

def func(name,age):
    print(f'my name is {name} and i m {age} yrs.')

func('rushal',21) #positional
func(age=21,name = 'rushal') #functional argument