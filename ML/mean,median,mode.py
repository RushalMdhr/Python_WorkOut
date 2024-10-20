# --------------------------------------------pip install numpy-----------------------------
import numpy

ar = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print(f'mean : {numpy.mean(ar)}')
print(f'median : {numpy.median(ar)}')


# --------------------------------------------pip install scipy-----------------------------
from scipy import stats 
print(f'mode : {stats.mode(ar)}')