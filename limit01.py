import numpy as np
import math
"""for i in range(0.1,1,0.01):
    for j in range(0.1,1,0.001):
        y=2*i*j/i**2+j**2
        print(y)
"""
for x in np.arange(-0.000000001,0,0.0000000001):
    y=x**2
    f=(x**2 *y)/(x**2+y**2)
print("the left limit is: ",f)
for x in np.arange(0.000000001,0,-0.0000000001):
    y=x**2
    f=(x**2 *y)/(x**2+y**2)
print("the right limit is: ",f)