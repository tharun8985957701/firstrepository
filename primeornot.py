n=int(input("enter any number: "))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
print(count)
if(count==2):
    print("given number is prime")
else:
    print("given number is not prime")