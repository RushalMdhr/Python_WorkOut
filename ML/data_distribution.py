import numpy

print(numpy.random.uniform(0.0, 5.0, 5))
import matplotlib.pyplot as plt
x= numpy.random.uniform(0.0, 5.0, 250)
plt.hist(x, 5)
plt.show()


#------------------------UNIFORM------------------------

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100)
plt.show()