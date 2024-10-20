import numpy
import matplotlib.pyplot as plt

#------------------------NORMAL------------------------

x = numpy.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()