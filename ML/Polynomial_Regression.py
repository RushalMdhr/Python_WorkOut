import matplotlib.pyplot as plt
import numpy


x = [1,2,3,4]
y = [2,4,6,8]

plt.scatter(x,y)
plt.show()  

mymodel = numpy.poly1d(numpy.polyfit(x,y,3))
myline = numpy.linspace(1, 4, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
