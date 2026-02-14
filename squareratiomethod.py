import math
n=int(input("enter no. of iterations you want to perform: "))
print("enter the points x1 and x2 based on IVT for the function: ")
x1=float(input("x1 = "))  #1
x2=float(input("x2 = "))   #2
print(f"a\t\t\tb\t\t\tf(a)\t\tf(b)\t\tc\t\tf(c)")
for i in range(1,n):
      y1=x1**2-2   #-1
      y2=x2**2-2   #2
      D=math.sqrt(y1**2/y2**2)
      c=(x1+x2*D)/(D+1)  
      y=c**2-2  
      print(f"{x1:.5f}\t\t{x2:.5f}\t\t{y1:.5f}\t\t{y2:.5f}\t\t{c:.7f}\t\t{y:.5f}")
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