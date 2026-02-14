"""n=int(input("enter no.of elements into the list: "))
l=[]
for i in range(n):
    element=int(input(f"enter {i} index element into the list: "))
    l.append(element)
print("the users list is: ",l)
max=l[0]
min=l[0]
for i in l:
    if(i>max):
        max=i
    if(i<min):
        min=i
print("the max and min elements in the list",max,min)
smax=l[0]
smin=l[0]
for i in l:
    if(i>smax & i!=max):
        smax=i
    if(i<smin & i!=min):
        smin=i
print("the smax and smin elements in the list are: ",smax,smin)
"""
s=[45,67,34,120,67,34,45,67,13,90]
maxE=s[0]
minE=s[0]
smaxE=s[0]
for i in s:
    if maxE<i:
        smaxE=maxE
        maxE=i
    elif(i>smaxE and i!=maxE):
        smaxE=i    
    else:
        if(minE>i):
            minE=i
print("maximum element of given list is :",maxE)
print("minimum element of given list is :",minE)
print("smaximum element of given list is :",smaxE)