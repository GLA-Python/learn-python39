# loop
# 1. for loop
# 2. while loop
c=0
x=int(input("enter the number"))
for i in range(1,x+1):
    if(x%i==0):
        c=c+1
if(c==2):
    print("prime no")
else:
    print("not a prime no")









