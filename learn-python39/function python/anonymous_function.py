# lambda function: we use the lambda keyword
# anonymous function: function without function name
# a function without name
# single executable statement based function *****
# we use lambda keyword to define the function.

# def function_name(a, b):
#     return a + b
#
# def sum_num(a, b):
#     return a**2 + b**2



# use of lambda with sorting the elemets
# sort()[method of list]
# sorted()[buit-in function]
# def apna_fun(x):
#     return x[-1]
#



# example 1 : square sum of two number
sum_num = lambda a, b : a ** 2 + b ** 2
V = sum_num(2, 5)
print(V)


# Example 2
# square
square = lambda x : x ** 2  # we dont use return keyword in lambda

print(square(10))


'''
syntax part

var_name = lambda ar1, ar2.. : expression (return statement)

'''
# example 3: with sort[built-in method list] or sorted[built-in function]
# def apna_fun(x):
#     return x[-1]

lst = ['ravi', 'priyanka', 'aman', 'aniket', 'ankit', 'sourabh']
print(lst)
# lst.sort(key=lambda x:x[-1])  # dont need of the return
lst = sorted(lst, key=lambda x:x[-1])
print(lst)

# ascii weight based sorting
# def apna_fun(x):  # x = 'ravi'
#     # logic
#     return sum([ord(i) for i in x])

# apna_fun = lambda x : sum([ord(i) for i in x])

lst = ['ravi', 'priyanka', 'aman', 'aniket', 'ankit', 'sourabh']
lst.sort(key=lambda x:sum([ord(i) for i in x]))
print(lst)

# Example 4: with map
# def apna_fun(x):
#     return x - 2

marks = [20, 65, 65, 23, 65, 54, 30]
V = list(map(lambda x:x-2, marks))
print(V)

# example 5: filter
# def apna_fun(x):
#     return x < 10

num_list = [1, 2, 43, 65, 75, 3, 7, 9, 4]
print(list(filter(lambda x: x<10, num_list)))

function_name = lambda a, b : a*b

v1 = 2
v2 = 10
V = function_name(v1, v2)
print(V)

# syntax
'''
variable = lambda argv list : executable statement
'''

sub = lambda a , b : a - b
re = sub(2, 4)
print(re)


# lambda function with map()
# def apna_fun(x):
#     return x - 2

# lambda
# apna_function = lamda x: x- 2
lst_marks = [20, 34, 22, 17, 33, 24]
print('old list ', lst_marks)
# using map function

new_lst_marks = list(map(lambda x: x * 2, lst_marks))
print(new_lst_marks)

# # 2. using list comprehension
# new_lst_marks = [i-2 for i in lst_marks]

# 3. using for loop
# new_lst_marks = []
# for i in lst_marks:
#     new_lst_marks.append(i - 2)
print('new updated list', new_lst_marks)

# sort()[list method] or sorted()[built-in]
# def apna_fun(x):  # x = 'ravi'
#     return x[-1]
# apna_fun = lambda x : x[-1]

lst = ['ravi', 'somya', 'ambika', 'rahul', 'ankit', 'aniket']
# lst.sort(key=lambda x : x[-1])  # didnt return
lst = sorted(key=lambda x:x[-1])
print(lst)


# sorted list with ascii-weight of the strings
lst = ['ravi','zzz', 'somya', 'ambika', 'rahul', 'ankit', 'aniket']
lst.sort(key=lambda x:sum([ord(i) for i in x ]))  # didnt return
print(lst)

# sorted list with length of the string
lst = ['ravi','zzz', 'somya', 'ambika', 'rahul', 'ankit', 'aniket']
lst.sort(key=len)  # didnt return
print(lst)

# reverse of the string in a list
lst = ['ravi','zzz', 'somya', 'ambika', 'rahul', 'ankit', 'aniket']
rlst = list(map(lambda x:x[::-1], lst))
print(lst)
print(rlst)



# filter(): to filter the elements with define properties
# def apna_fun(x):
#     return x < 10
#
# apna_fun = lambda x: x < 10

lst = [2, 4, [], [2], (), (4, 5), [5], '', 'hi', 0]

out = list(filter(lambda x: x, lst))
print(out)


# filter the even numbers
lst = list(range(1, 21))
lst = list(filter(lambda a: a % 2 == 0, lst))
print(lst)


def function():
    x = 23
    y = 43


print(function.__code__.co_varnames)

a = 221
# h = a + 20
h = a.__add__(20)
print(h)














