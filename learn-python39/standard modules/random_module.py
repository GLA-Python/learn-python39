"""
Random Module in Python: random variable generators
Modules in Python: just a python file where function defines
"""
import random

v2 = random.randrange(1, 101)
count = 0
while 1:
    v1 = int(input('enter the number '))
    count += 1
    if v2 < v1:
        print('number is greater')
    elif v2 > v1:
        print('value is smaller')
    else:
        print('right number with count ', count)
        break


# randrange(): return a number with given range
import random
v = random.randrange(1, 10)
print(v)


# randint(): return a int number with inclusive range
import random
v = random.randint(1, 147)
print(v) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# shuffle(): shuffle the list elements
lst = [1, 2, 3, 5, 7, 8]
random.shuffle(lst)
print(lst)

# choice
lst = ['ravi', 'salman', 'muskan']
name = random.choice(lst)
print(name)


# choices()
lst = ['ravi', 'salman', 'muskan']
name = random.choices(lst, weights=(1, 4, 2), k = 3)
print(name)


# sample():
lst = ['ravi', 'salman', 'muskan']
name = random.sample(lst, k=2)
print(name)





