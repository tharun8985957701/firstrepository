import numpy as np
import math
for i in np.arange(-2,2,0.01):
    for j in np.arange(-2,2,0.01):
        if(math.sqrt(i**2+j**2)<2):
            z=(i*j)/math.sqrt(i**2+j**2)
            print(z)
            if(-1>z or z>1):
                print(i,j)
            else:
                print("win")