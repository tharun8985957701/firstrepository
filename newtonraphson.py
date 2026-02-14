"""x=1
for i in range(1,32):
    x=(2*x**3 + 6)/(3*x**2 -5)
    y=x**3-5*x+6
    print(x,',',y)
"""
n=int(input("enter no. of iterations to perform: "))
x=float(input("enter initial point to find approx root by newton raphson method: "))
print("x\t\t\tf(x)\t\t\t\tf'(x)\t\t\t\tc\t\t\t\tf(c)")
for i in range(1,n+1):
    x1=x
    y1=(1/x1)-9
    dydx=-1/x**2
    x2=x1-(y1/dydx)
    y2=(1/x2)-9
    print(f"|{x1:.4f}|\t\t|{y1:.5f}|\t\t\t|{dydx:.4f}|\t\t|{x2:.4f}|\t\t\t|{y2:.5f}|")
    x=x2
print("\n""the approximate root of given function is: ",x*2)