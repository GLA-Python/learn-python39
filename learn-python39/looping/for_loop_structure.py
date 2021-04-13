# loop
# 1. for loop
# 2. while loop

# 1. for loop
# iterting or iteration over the sequence
'''
for index in sequential_entity:
    # for body
'''
'''
C- Programming : for loop work with comparison 
for(int i=0; i<100; i++)
    {
        printf("Hello");
        i = 99;
    }
Python3 : for loop work with assignment 
for i in [0, 1, 2, 3, 4, 5]:
    print("Hello", i)  
    i = 99  
    
'''


# example sum of list
s = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    s = s + i
    break
else:
    print('loop completed')
print(f'natural sum is {s}')

# double index in for loop
x = [[1,2], [2, 3], [3, 3], 'Hi']
for i, j in x:  # i, j = x[0]
    print(i)


c=0
x=int(input("enter the number"))
for i in range(1,x+1):
    if(x%i==0):
        c=c+1
if(c==2):
    print("prime no")
else:
    print("not a prime no")



# else part with for loop
# home work




