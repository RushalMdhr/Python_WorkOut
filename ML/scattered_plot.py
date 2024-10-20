import numpy
import matplotlib.pyplot as plt
# JUST LIKE PLOTING X AND Y IN 2D GRAPH 
x = [1,5,10]
y = [1,5,10]

plt.scatter(x, y)
plt.show()


#------------------------NORMAL------------------------

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()


#------------------------UNIFORM------------------------
x = numpy.random.uniform(5.0, 1.0, 1000)
y = numpy.random.uniform(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()