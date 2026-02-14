#01 function
#x="""function is relation from one set to another,
#it works like a machine i.e,for every input value it give outputs and
#by horizontal line test we can confirm which are functions.""" 
#print("function: ",x)
#print("the example of functions are:  ")
#print("x ,x^3 ,e^x ,logx ,sinx ; -π/2 <= x <= π/2 etc...")

"""
#02 slope
y="th e slope(m) of a function is the tangent of angle of inclination(θ) from line to +ve x-axis."
print("slope: ",y)
print("--","the slope of f(x) is also called as derivative of that function at that point,f'(x)")

# 03 slope of a line
print("the slope of a line passing through the points (x1,y1) and (x2,y2) is:  ")
print(               )
print("                                (y2-y1)/(x2-x1)")


#04 angle of inclination
print("given that the function is y=x")
print("it is the line passing through origin,having m=1")
import math
θ=tan^(-1)(m)
print("the value of θ is : ",θ)

import math
import matplotlib.pyplot as plt

x_values=[]
y_values=[]
dx=[]
dy=[]
derivative=[]
 
x=0
while x<=2*math.pi:
    x_values.append(x)
    y=math.sin(x)
    y_values.append(y)
    x+=0.1

for i in range(len(x_values)-1):
    dx.append(x_values[i+1]-x_values[i])
    dy.append(y_values[i+1]-y_values[i])

for i in range(len(dx)):
    derivative.append(dy[i]/dx[i])

print('x\tsin(x)\tdx\tdy\tdy/dx')
for i in range(len(derivative)):
    print(f'{x_values[i]:.2f}\t{y_values[i]:.2f}\t{dx[i]:.2f}\t{dy[i]:.2f}\t{derivative[i]:.2f}')

plt.plot(x_values[:-1],derivative,label='approximated derivative')
plt.plot(x_values,[math.cos(x) for x in x_values],linestyle='dashed',label='cos(x)')
plt.legend()
plt.title("derivative of sin(x)")
plt.xlabel("x")
plt.ylabel("dy/dx")
plt.grid(True)
plt.show()


y_values=[]
rate_of_change=[]
dx=1
n=int(input("enter the number of x values to generate: "))
for x in range(0,n):
    y=x
    y_values.append(y)
for x in range(n-1):
    dy=y_values[x+1]-y_values[x]
    rate_of_change.append(dy/dx)
print("x  | dx  | dy | dy/dx")
print("-------------------------")
for x in range(0,n-1):
    dy=y_values[x+1]-y_values[x]
    rate=rate_of_change[x]
    print(f"{x} | {dx} | {dy} | {rate}")

    
y_values=[]
dydx=[]
dx=1
n=int(input("the number of x_values upto what"))
for i in range(n):
    y=i**2
    y_values.append(y)
print("x  | dx  | dy | dy/dx")
for i in range(0,n-1):
    dy=y_values[i+1]-y_values[i]
    m=dy/dx
    dydx.append(m)
    print("-------------------------")
    print(f"{i}  |  {dx}  | {dy} | {m}")

    
n=int(input("enter a number upto what you have to generate: "))
for i in range(n):
    print(i)
print("-------------------------")
for i in range(0,n):
    print(i)
print("-------------------------")
for i in range(n-1):
    print(i)
print("-------------------------")
for i in range(0,n-1):
    print(i)

x_values=[]
y_values=[]
dx=[]
dy=[]
dydx=[]
n=int(input("enter a number upto what it should be generate: "))
for i in range(n):
    x=i
    x_values.append(x)
    y=i**2
    y_values.append(y)
for i in range(n-1):
    dx.append(x_values[i+1]-x_values[i])
    dy.append(y_values[i+1]-y_values[i])
for i in range(n-1):
    dydx.append(dy[i]/dx[i])
print("|  x  |  y  |    dx  |      dy  |       dy/dx  |")
print("------------------------------------------------")
for i in range(n-1):
    print(f"| {x_values[i]}   |   {y_values[i]}   |   {dx[i]}    |  {dy[i]}     |      {dydx[i]} |")

import math
x_values=[]
y_values=[]
dx=[]
dy=[]
dydx=[]
n=int(input("enter a number upto what it should be generate: "))
for i in range(n):
    x=i
    x_values.append(x)
    y=math.sqrt(x)
    y_values.append(y)
for i in range(n-1):
    dx.append(x_values[i+1]-x_values[i])
    dy.append(y_values[i+1]-y_values[i])
for i in range(n-1):
    dydx.append(dy[i]/dx[i])
print("|  x  |  y  |    dx  |      dy  |       dy/dx  |")
print("------------------------------------------------")
for i in range(n-1):
    print(f"| {x_values[i]}   |   {y_values[i]:.2f}   |   {dx[i]:.2f}    |  {dy[i]:.2f}     |      {dydx[i]:.2f} |")

import math
x_values=[]
y_values=[]
dx=[]
dy=[]
dydx=[]
n=int(input("enter a number upto what it should be generate: "))
for i in range(n):
    x=i
    x_values.append(x)
    y=math.exp(x)
    y_values.append(y)
for i in range(n-1):
    dx.append(x_values[i+1]-x_values[i])
    dy.append(y_values[i+1]-y_values[i])
for i in range(n-1):
    dydx.append(dy[i]/dx[i])
print("|  x  |  y  |    dx  |      dy  |       dy/dx  |")
print("------------------------------------------------")
for i in range(n-1):
    print(f"| {x_values[i]}   |   {y_values[i]:.2f}   |   {dx[i]:.2f}    |  {dy[i]:.2f}     |      {dydx[i]:.2f} |")

import math
import matplotlib.pyplot as graph
x_values=[]
y_values=[]
dx=[]
dy=[]
dydx=[]

x=0
while(x<=2*math.pi):
    x_values.append(x)
    y=math.sin(x)
    y_values.append(y)
    x=x+0.1
for i in range(len(x_values)-1):
    dx.append(x_values[i+1]-x_values[i])
    dy.append(y_values[i+1]-y_values[i])
for i in range(len(dx)):
    dydx.append(dy[i]/dx[i])
print("|  x      |      y  |      dx  |      dy  |       dy/dx  |")
print("----------------------------------------------------------")
for i in range(len(dydx)):
    print(f"| {x_values[i]:.2f}   |   {y_values[i]:.2f}   |   {dx[i]:.2f}    |  {dy[i]:.2f}     |      {dydx[i]:.2f} |")

graph.plot(x_values[:-1],dydx,label='approximated derivative')
graph.plot(x_values,[math.cos(x) for x in x_values],linestyle='dashed',label='cos(x)')
graph.legend()
graph.title("derivative of sin(x)")
graph.xlabel("x")
graph.ylabel("dy/dx")
graph.grid(True)
graph.show()

import math
x_values=[]
y_values=[]
dx=[]
dy=[]
dydx=[]
x=0
while(x<=6*math.pi):
    x_values.append(x)
    y=math.cos(x)
    y_values.append(y)
    x=x+0.1
for i in range(len(x_values)-1):
    dx.append(x_values[i+1]-x_values[i])
    dy.append(y_values[i+1]-y_values[i])
for i in range(len(dx)):
    dydx.append(dy[i]/dx[i])
print("|  x      |      y  |      dx  |      dy  |       dy/dx  |")
print("----------------------------------------------------------")
for i in range(len(dydx)):
    print(f"| {x_values[i]:.2f}   |   {y_values[i]:.2f}   |   {dx[i]:.2f}    |  {dy[i]:.2f}     |      {dydx[i]:.2f} |")

import matplotlib.pyplot as graph
graph.plot(x_values[:-1],dydx,label='approximated derivative')
graph.plot(x_values,[math.sin(x) for x in x_values],linestyle='dashed',label='sin(x)')
graph.legend()
graph.title("derivative of cos(x)")
graph.xlabel("x")
graph.ylabel("dy/dx")
graph.grid(True)
graph.show()
"""
import math
import matplotlib.pyplot as plt
x_values=[]
y_values=[]
derivative=[]
lineequations=[]
points=[(x,y)for x in range(-4,5) for y in range(-4,5)]
for x,y in points:
    x_values.append(x)
    y_values.append(y)
for x,y in points:
    if (y==0):
        print("--")
        lineequations.append(f'{"x=",x}')
    else:
        m=int(-x/y)
        derivative.append(m)
for i in range(len(derivative)-1):
    b=y_values[i]-(derivative[i])*(x_values[i])
    equation=f'{m}x+{b:.1f}'
    lineequations.append(equation)
print("x\t\ty\t\t(x,y)\t\t\tslope\t\t\tline_equation")
print("---------------------------------------------")
for i in range(len(derivative)-1):
    print(f'{x_values[i]}\t\t{y_values[i]}\t\t{(x_values[i],y_values[i])}\t\t\t{derivative[i]}\t\t\t{lineequations[i]}')
for i in range(len(derivative)-1):
    plt.quiver(x_values[i],y_values[i],y_values[i],-x_values[i])
    plt.xlim(-4,4)
    plt.ylim(-4,4)
    plt.grid(True)
    plt.show()




