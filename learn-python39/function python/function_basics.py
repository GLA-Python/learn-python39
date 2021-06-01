"""
function : group of related statements which perform a specific task
function:
    1. built-in function
    2. user define
"""

k = ord('A')  # return the unicode code of guiven char
print(k)
# v = [2, 4, 5, 89, 45, 3, 5, 3, 5]
# v = 'hello'
v = 122  # TypeError: 'int' object is not iterable
mx = max(v)
print('maximum value is ', mx)  #

# user define function
# how function handle the arg in Python
# how return work in python

# function syntax
'''
def function_name(list of argv):
        # function body 
        # return statment (default return is None)

'''

# write a python program to check the given number is prime or not?

def prime(num):  #  num(local) = num(actual)
    i = 1
    count = 0
    while i <= num:
        if num % i == 0:
            count += 1
        i += 1
    if count == 2:
        return True
    else:
        return False

def perfect(N):  # N = num(global or actual)
    f_sum = 0
    # logic here
    i = 1
    while i < N:
        if N % i == 0:
            f_sum += i
        i += 1
    if f_sum == N:
        return True
    else:
        return False




num = int(input('enter the positive integer number '))
v = prime(num)
p = perfect(num)
print('number is prime') if v else print('number is not prime')
print('perfect number ') if p else print('not perfect ')















