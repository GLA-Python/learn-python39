# loop
# iterting or iteration over the sequence
# 1. for loop
# 2. while loop

'''
for index in sequential_entity:
    # for body
'''
x = [1, 3, 4]
for i in x:
    print(i)
    x[1] = 100
print(x)













c=0
x=int(input("enter the number"))
for i in range(1,x+1):
    if(x%i==0):
        c=c+1
if(c==2):
    print("prime no")
else:
    print("not a prime no")









