"""
function : group of related statements which perform a specific task
function:
    1. built-in function
    2. user define function(UDF)
"""
# how built-in work
# example 1(min)
v = [3, 54, 65, 64]
y = min(v)  # function calling
print('minimum value in collection v', y)

# example 2 (max)
ls = [2, 4, 5, 645, 543]
mx = max(ls)
print(mx)

k = 100
v = min(k)
print(v)

# function in Python
# WAP to check the number is prime or not
def prime(num):  # num(local) = num(global)
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

def perfect(k):  # k(local) = num(global)
    f_sum = 0
    i = 1
    # logic here
    while i < k:
        if k % i == 0:
            f_sum += i
        i += 1
    if f_sum == k:
        return True
    else:
        return False
num = int(input('enter the positive integer '))
V = prime(num)
U = perfect(num)
print('Number is prime ') if V else print('Number is not prime ')
print('perfect number ') if U else print('not a perfect number ')

# function synatx
'''
def function_name(argvs):
    # main logic
    # return statements(default return from any function is None)

'''
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

# Type of Arguments
'''
1. actual arg
    a) positional arguments
    b) keyword arguments
2. formal
'''

# example for positional arguments
def sum_num(a, b, c, m):
    return a**2 + (b + c) * m

x = 2
y = 3
r = 4
z = 0
sum_num(y, x, r, z)


# function syntax
'''
def function_name(list of argv):
        # function body 
        # return statment (default return is None)

'''


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
# function calling
'''
# Type of arguments:
    1. positional arguments
        a) optional positinal arguments 
    2. keyword arguments
        a) optional keyword arguments  

'''

# positional arguments
# example 1
def sum_num(x, y, z):  # x = 3, y = 6
    return x**2 + y**3 + z

H = sum_num(6, 5, 10)  # function calling with positional argv
print(H)

# variable length argument or optional positional arguments
# example 2
def sum_num(x, y, *var):  # x = 3, y = 6
    s = x+y
    for i in var:
        s += i
    return s

H = sum_num(2, 5, 3)  # function calling with positional argv
print(H)


# example3
def sum_num(*var, x, y):  # x = 3, y = 6
    s = x+y
    for i in var:
        s += i
    return s

H = sum_num(2, 5, 3,4, x=2, y=0 )  # function calling with positional argv
print(H)

# default arguments
# example 4
def display(*x, sep=' ', end='\n'):  # x = 3, y = 6
    st_lst = list(map(str, x))
    f = sep.join(st_lst)
    print(f, end=end)

display(2, 4, 6, 7, 'amir', sep='\n', end='')
display('hello')




# keyword arguments
def student_info(name, section, roll_number, subject):
    # logic
    info = f'''
        Name : {name}
        Section : {section}
        Roll Number: {roll_number}
        subject : {subject} 
    '''
    return info

k = student_info('manish', 3, 'E', 'Python')  # positional argv
print(k)

V = student_info( roll_number=34,  section='E', subject='Python Programming', name='ravi')  # function calling using keyword argv
print(V)


# example 2: with  optional keyword arguments
def student_info( **dct):
    # logic
    info = f'''
        Name : {dct.get('name')}
        Section : {dct.get('section')}
        Roll Number: {dct.get('roll_number')}
        subject : {dct.get('subject')} 
    '''
    return info
V = student_info( subject='Python')  # function calling
print(V)


# how to handle the default value arguments in Python function
def sum_num( a=0, b=0, c=3):  # a = 3, b = 5, c = 7
    return a + b + c

v = sum_num(3, 5, 6)
print(v)





# keyword arguments (optional)
def student_info( **var):
    # logic
    print(var)
    info = f'''
        Name : {var.get('name')}
        Section : {var.get('section')}
        Roll Number: {var.get('roll_number')}
        subject : {var.get('subject')} 
    '''
    return info

k = student_info( subject='math', name='ravi', cpi=8.5)
print(k)



# variable scope
'''
1. local
2. global
3. nonlocal 
'''
def fun():
    a = 33  # local variable

a = 12  # global variable
fun()
print(a)
# output :=> 12


def info():
    def second():
        var = 12  # local variable
    def third():
        var = 43  # local variable
    def fourth():
        var = 0   # local variable
    var = 100  # local varibale
    second()
    print(var)
    third()
    print(var)
    fourth()
    print(var)

var = 10  # global variable
info()
print(var)




# read global data
def xml():
    # var = 10
    print(var)  # referencing with global

var = 100  # global
xml()  # function calling
print(var)  # read var

# output
100
100

# write in global with local
def xml():
    global var
    print(var)  # local variable var


def xml2():
    print(var)

xml()
xml2()
print(var)



#
def info():
    def second():
        var = 12  # local variable
    def third():
        nonlocal var
        var = 43  # local variable
    def fourth():
        global var
        var = 0   # local variable
     # local varibale
    var = 100 # nonlocal environment
    second()
    print(var)
    third()
    print(var)
    fourth()
    print(var)

var = 22  # global variable
info()
print(var)







# scope of variable (important**)
def info():
    a = 'veg'  # local

info()  # function execute
a = 'non-veg'  # global
print(a)  # veg

# variable scope in a function
'''
1. local: variable inside a function 
2. global: variable outside the function 
3. nonlocal: variable inside a function of function(nested function) 
'''

def info():
    def second():
        var = 0  # local variable
    def third():
        global var
        var = 22
    def fourth():
        nonlocal var
        var = 1

    var = 10  # nonlocal variable
    second()
    print(var)
    third()
    print(var)
    fourth()
    print(var)

var = 100  # global variable
info()
print(var)

# global read inside a

def fun():
    print(k*3)  # k is global
    k = 23  # k is local


k = 100
fun()
# example based on scope


def any_two(var):  # var = var
    def hlt():
        global var
        print(var)


var = 33
any_two(var)