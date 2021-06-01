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

# ls = [3, 5, 6, 16, 34]
# for c, k in [[3, 43], [3, 43]]:
#     print(c, k)
#
#
# print(list(enumerate({3, 5, 7})))

# function body : where we write the main logic

# function calling: we call the function for execution
v = prime(10)  # False
print(v)
v = prime(18, 23)  # prime() takes 1 positional argument but 2 were given
print(v)
'''
# Type of arguments:
    1. positional arguments
    2. keyword arguments 

'''
# 1. positional arguments: every arg having fixed position
# example 1: sum of Three number
def sum_num(x, y, z):  # x = a, y = b, z = c
    return x + y + z

a, b, c = map(int, input().split())
s = sum_num(a, b, c)
print(f'Sum of {a}, {b} and {c} is {s}')

# 2. keyword arguments: call parameter by name
def sum_num(first, second, third):  # x = a, y = b, z = c
    return first**2 + second**3 + third**4

a, b, c = map(int, input().split())
s = sum_num(a, c, b)  # function calling with positional argv
s = sum_num(first = a, third = c, second = b)  # function calling with keyword arguments
print(f'Sum of {a}, {b} and {c} is {s}')

# example 2: students info
def students_info(name, roll_number, section, subject):
    info = f'''
        Name : {name}
        Section : {section}
        Roll Number: {roll_number}
        Subject: {subject}
    '''
    print(info)


students_info('vishnu', 23, 'C', 'Python Programming')  # function calling with positional argv
students_info( section='C', roll_number=32, subject='Math', name='Rahul')  # functiona calling with keyword argv











