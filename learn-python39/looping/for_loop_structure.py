# loop

# 1. for loop
# 2. while loop

# 1. for loop
# iterting or iteration over the sequence
'''
for index in sequential_entity:
    # for body
'''

s = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    s = s + i
    break
else:
    print('loop completed')
print(f'natural sum is {s}')















c=0
x=int(input("enter the number"))
for i in range(1,x+1):
    if(x%i==0):
        c=c+1
if(c==2):
    print("prime no")
else:
    print("not a prime no")









