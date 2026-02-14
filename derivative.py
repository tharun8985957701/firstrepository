"""
y=1
n=int(input("enter a number upto to what"))
for i in range(n+1):
    x1=i,x2=i+1
    y1=1,y2=1
    dx=x2-x1
    dy=y2-y1
    print(dy/dx)


n=int(input("enter a number upto to what"))
for i in range(n+1):
    x1=i
    y1=i
    x2=i+1
    y2=i+1
    dx=x2-x1
    dy=y2-y1
    print(f"x={x1},y={y1},dx={dx},dy={dy},dy/dx={dy/dx}")
"""
import math
n=int(input("enter a number upto to what: "))
f=input("enter the function: ")
for i in range(n+1):
    x1=i
    y1=eval("x1")
    x2=i+1
    y2=eval(f.replace("x1",str(x2)))
    dx=x2-x1
    dy=y2-y1
    dydx=dy/dx
    print(f"x={x1},y={y1},dx={dx},dy={dy},dy/dx={dydx}")

import matplotlib.pyplot as plt
plt.plot(x1,dydx)
plt.show()


