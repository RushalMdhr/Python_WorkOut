names = ['rushal','rush','mheteula','ola']

def change(name):
    if name in names:
        i=names.index(name)
        x=input('change to what?: ')
        names[i]=x
        print(names)
print(names)
change(input('name to change : '))