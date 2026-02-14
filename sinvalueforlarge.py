import math
x=float(input("enter the angle in radians to calculate: ")) #8985957701
if(0<x<2*math.pi):
    print("the value of sinx is: ",math.sin(x))
else:
    I=x//(2*math.pi) 
    print("the no. of cycles to rotate:",I)
    x=x-(I*2*math.pi)
    print("the angle after ",I," cycles is ",x)
    print("the value of sinx is: ",math.sin(x))
    print("\n")
    print("the value of x:",x)
    y=(3.3227596282958984)-((3.3227596282958984**3)/6)+((3.3227596282958984**5)/120)-((3.3227596282958984**7)/5040)+((3.3227596282958984**9)/)
    print("the value of y which exactly fitting polynomial for sinx in range (0,2*pi): ",y)
print("the value of sine: ",math.sin(3.3227596282958984))