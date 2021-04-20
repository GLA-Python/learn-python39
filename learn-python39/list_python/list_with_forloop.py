# lst1 = [2, 4, 5, [2, 4]]
# lst2 = lst1.copy()
# lst1[-1].clear()
# print(lst1)
# print(lst2)



# for loop structure
'''
for variable in sequential(list, tuple, string):
    # loop body
'''

# example 0
# print all natural number upto the N
N = 20
x = range(1, N+1)
for i in x:  # i = 1
    print(i, end=' ')

#
# # all natural number range upto N
# N = 6
# x = range(1, N)  # [1, 2, 3, 4, 5, 6]
#
# re = range(-2)
# print(list(re))


re = list(range(-2))  # start 0 stop -2 step 1
print(re)  # []

'''
range(start, stop, step)  # generate the sequential data 
1. with single arguments 
re = range(10)
start 0  default 
stop 10
step 1  default 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

re = list(range(1, 4))  # start 1 stop 4 step 1
print(re)  # [1, 2, 3]

re = list(range(10, 4))  # start 10 stop 4 step 1
print(re)  # []

re = list(range(-1, -4))  # start -1 stop -4 step 1
print(re)  # []

re = list(range(-4, -1))  # start -4 stop -1 step 1
print(re)  # [-4, -3, -2]

'''
2. with 2 arguments 
re = range(1, 4)
start = 1 update
stop = 4 update 
step = 1 default 

[1, 2, 3]
'''

re = list(range(1, 10, 3))  # start 1 stop 10 step 3
print(re)  # [1, 4, 7]

re = list(range(-10, -1, -2))  # start -10 stop -1 step -2
print(re)  # []

re = list(range(-1, -10, -2))  # start -1 stop -10 step -2
print(re)  # [-1, -3, -5, -7, -9]

'''
3. with 3 arguments 
re = range(1, 4, 2)
start = 1 update
stop = 4 update 
step = 2 update
[1, 3]
'''

# x =   # 10 9 8 7 6 5 4 3 2
for i in range(10, 1, -1):
    print(i)

for i in 'hello':
    print(i)

x = [2, 4, 5]
for i in x:
    print(i)
    x.clear()
# output
# 2

# infinite loop using for loop
x = [2, 4]
for i in x:
    print(i)
    x.append(10)




# else part of for-loop
for i in range(10):  # 1 4 7
   print(i)
   if i >= 4:
        break
else:
    print('loop completed')


# list value assignment to other variable
lst1 = [2, 4]
lst2 = lst1
lst1[0] = 'Python'
lst1.append(100)
print(f'lst1 {lst1}')
print(f'lst2 {lst2}')


# example 2
x = [2, 4, 5]
for i in x:
    print(i)
    i = 5
    x = 100

# output
# 2
# 4
# 5

else:
    print('loop completed')

# output
# 2
# loop completed

# example 4
x = [2, 4, 5]
for i in x:
    print(i)
    x.clear()
# Output
# 2


# example 3: infinite loop using for loop
x = [2, 4, 5]
for i in x:
    print(i)
    x.append(10)
else:  # optional
    print('loop completed')

# output
# 2
# 4
# 5
# 10........


# example 4
x = [2, 4, 5]
for i in x:
    print(i)
    if i == 4:
        break
else:
    print('loop completed')
# output
# 2
# 4


# prime number without using third variable
num = 5
for i in range(2, num):  # 2 3 4
    if num % i == 0:
        print(f'number {num} is not prime ')
        break
else:
    print(f'number {num} is prime ')




