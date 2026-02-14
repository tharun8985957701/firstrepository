"""
n=int(input("enter no. of iterations you want to perform: "))
print("enter the points x1 and x2 based on IVT for the function: ")
x1=int(input("x1 = "))  #-3
x2=int(input("x2 = "))  # -2
print(f"a\t\t\tb\t\t\tf(a)\t\t\tf(b)\t\t\tc\t\t\tf(c)")
for i in range(1,n):
    y1=x1**3-5*x1+6 # -6
    y2=x2**3-5*x2+6  # 8
    c=(x1+x2)/2  #-2.5
    y=c**3-5*c+6  #2.875
    print(f"{x1:.5f}\t\t{x2:.5f}\t\t{y1:.5f}\t\t{y2:.5f}\t\t{c:.5f}\t\t{y:.5f}")
    if(y>0):
        if(y1>0):
            x1=c
            x2=x2
        if(y2>0):
            x1=x1
            x2=c
    else:
        if(y1<0):
            x1=c
            x2=x2
        if(y2<0):
            x1=x1
            x2=c
print("\n")
print("the approximate root of given function is: ",c)

"""
import math       
n=int(input("enter no. of iterations you want to perform: "))
print("enter the points x1 and x2 based on IVT for the function: ")
x1=int(input("x1 = "))  #0
x2=int(input("x2 = "))  #1
print(f"a\t\t\tb\t\t\tf(a)\t\t\tf(b)\t\t\tc\t\t\tf(c)")
for i in range(1,n):
    y1=x1*(math.e)**x1-1 # -1
    y2=x2*(math.e)**x2-1  # e-1
    c=(x1+x2)/2  #0.5
    y=c*(math.e)**c-1  #-0.175639
    print(f"{x1:.5f}\t\t{x2:.5f}\t\t{y1:.5f}\t\t{y2:.5f}\t\t{c:.5f}\t\t{y:.5f}")
    if(y>0):
        if(y1>0):
            x1=c
            x2=x2
        if(y2>0):
            x1=x1
            x2=c
    else:
        if(y1<0):
            x1=c
            x2=x2
        if(y2<0):
            x1=x1
            x2=c
print("\n")
print("the approximate root of given function is: ",c)
