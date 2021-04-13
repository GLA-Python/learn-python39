"""
list in Python: ordered collection of items enclose within []
sequence of object
"""

# how to initialize the string
# empty
lst = []  # list format
lst = list()  # using list class constructor
print(lst)

# with value(items)
lst = [2, 65, 'hello', [3, 55], 2.55, 43+5j]
print(lst)

# accessing the elements in list
# indexing : indexing generate error if index value >= len()
lst = [2, 65, 'hello', [3, 55], 2.55, 43+5j]
ele = lst[-1]
print(ele, type(ele))
# st = 'hello'
# ele = st[0]
# print(ele, type(ele))

# slicing : sublist from the list : no error with wrong range
# example 1
lst = [2, 65, 'hello', [3, 55], 2.55, 43+5j]
sublist = lst[1:2]  # 1
print(sublist, type(sublist))  # Output [65] class type list

# example 2
lst = [2, 65, 'hello', [3, 55], 2.55, 43+5j]
sublist = lst[-1:-4]  # no range
print(sublist, type(sublist))  # [] class list

# example 3
lst = [2, 65, 'hello', [3, 55], 2.55, 43+5j]
sublist = lst[-4:-1]  #  -ve:- -4 -3 -2       +ve:- 2 3 4
print(sublist, type(sublist)) # Output ['hello', [2, 55], 2.55]


# why list is mutable
# mutable property of list
# 1. item assignment
lst = [2, 65, 'hello', [3, 55], 2.55, 43+5j]
print(f'before item assignment id {id(lst)} and value {lst}')
lst[0] = 'Hi'  # item assignment
print(f'after item assignment id {id(lst)} and value {lst}')

# 2. insert items
lst = [2, 65, 'hello', [3, 55], 2.55, 43+5j]
lst.append(100)
print(lst)














