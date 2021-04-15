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
x = [2, 4, 5]
for i in x:
    print(i)
    i = 57346638563456345346534563476534567345683467
    x = 10
else:
    print('loop completed')

# example 2
x = [2, 4, 5]
for i in x:
    print(i)
    x.clear()
else:
    print('loop completed')

# output
# 2
# loop completed


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
for i in range(2, num):
    if num % i == 0:
        print('Not prime a prime number ')
        break
else:
    print('Prime number ')



