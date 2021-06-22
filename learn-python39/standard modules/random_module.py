"""
Random Module in Python: random variable generators
Modules in Python: just a python file where function defines
"""

import random

lst = [2, 4, 55, 32, 3, 67, 23]

v   = random.choice(lst)

print(v)


# choice(): return the random single value from sequential data

import random
names = ['raj', 'ravi', 'muskan', 'ayush']
name = random.choice(names)
print(name)


# randrange(): return a interger number between given range

import random
num = random.randrange(1, 10, 5)  # 1, 6
print(num)



# guess the number
import random
num = random.randrange(1, 101)
count = 0
while 1:
    n = int(input('guess the number '))
    count += 1
    if n < num:
        print('smaller number ')
    elif n > num:
        print('number is greater ')
    else:
        print('You Win score/', count)
        break



# randint(): return a random number between a and b inclusive

import random
v = random.randint(1, 4)  # 1, 2, 3, 4
print(v)


# choices(): return multiple choice
import random
lst = ['ravi', 'yash', 'satrughan sinha', 'salman khan']
ch = random.choices(lst, weights=(1, 1, 5, 2), k=3)
print(ch)


# sample()
lst = ['ravi', 'yash', 'satrughan sinha', 'salman khan']
ch = random.sample(lst, k=2)
print(ch)



# shuffle(): use to shuffle the list
lst = ['ravi', 'yash', 'satrughan sinha', 'salman khan']
random.shuffle(lst)
print(lst)




# random()

import random

v = random.random()

print(v)



# opt of 4 digit
import random
otp = str(random.random())[-4:]
print(otp)



# seed()
import random
rg = random.randrange(1, 10)  # 1, 2, 3, 4, 5, 6, 7,8, 9
print(rg)




'''
3 8 8 3 7

'''




import random
lst = ['ravi', 'saket', 'maryam', 'shaurabh']
name = random.choice(lst)
print(name)








'''
saket
shaurabh
shaurabh
saket


'''



































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





