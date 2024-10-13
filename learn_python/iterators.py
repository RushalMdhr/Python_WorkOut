a=(1,2,3)
b=iter(a)

print(next(b))
# print(b)
print(next(b))
#---------------------------------------------creating an iterator
print('creating an iterator : ')
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

for x in range(8):
    print(next(myiter))

