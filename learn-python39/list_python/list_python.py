"""
Python list : ordered collection of items(object)
sequence of object
"""

# how to initialize the list
# empty
lst = []  # list format
lst = list()  # list class constructor
print(lst)


# initialize list with some items
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
print(lst)  # Output [12, 32.8, (22+3j), 'hello', [3, 43]]


# accessing the elements
# 1. indexing
# 2. slicing
# indexing : get the single element at position(index)
# will generate the error if index value >= len()
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
re = lst[0]  # indexing
print(re, type(re))  # Output 12 <class 'int'>

# slicing : sublist from list
# in slicing no error if wrong range passed
# example 1
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
re = lst[::1]  # 0 1 2 3 4
print(re, type(re))  # [12, 32.8, 22+3j, 'hello', [3, 43]] class<list>

# example 2
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
re = lst[1:2]  # 1
print(re, type(re))  # 32.8 class<list>

# example 3
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
re = lst[-1:-4] # no range
print(re, type(re))

# example 4
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
re = lst[1:4:-1] # no range
print(re, type(re))

# example 5
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
re = lst[4:1:-1] # range 4, 3, 2
print(re, type(re))  # [[3, 43], 'hello', (22+3j)] class<list>

# example 6
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
re = lst[4:-1:-1] # no range
print(re, type(re))  # [] class<list>

# how list is mutable
# mutable property of list
# 1. item assignment
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
print(f'before item assignment value {lst} and id {id(lst)}')
lst[0] = 'Python'
print(f'after item assignment value {lst} and id {id(lst)}')


# 2. append values
lst = [12, 32.8, 22+3j, 'hello', [3, 43]]
lst.append(100)
print(lst)

