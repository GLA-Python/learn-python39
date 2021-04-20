"""
Python list : ordered collection of items(object)
sequence of object
"""

# how to initialize the list
# empty
lst = []  # list format
lst = list()  # list class constructor
print(lst)

k = 'hello'
print(ord(k[0]))
lst = list(k)
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





# 1. append(): add the element or item at the end of the list
lst = [2, 43, 'Hello', [3, 5]]  # len 4
lst.append('Python')  # len 5
lst.append([2, 4, 54])  # len 6
lst.append(100) # len 7
print(lst)
# Output [2, 43, 'Hello', [3, 5], 'Python', [2, 4, 54], 100]

# 2. extend: add the list or iterable items in a current list
lst = [2, 43, 'Hello', [3, 5]]  # len 4
lst.extend([100, 120, 130])  # len 4 + 3 = 7
# lst.extend(100)  # generate error 'int' object is not iterable
lst.extend('Hello')
print(lst)

# 3. insert : add the element at position
lst = [2, 43, 'Hello', [3, 5]]
lst.insert(0, 'Python')
print(lst)


# 4. clear : remove all the items in a list
lst = [2, 43, 100, 'hello']
lst.clear()
print(lst)

# 5. pop(): remove the element at specified index
lst = [2, 4, 34, 100, [2, 43]]
ele = lst.pop(3)  # remove the item at given index 3 and return value 100
print(f'element {ele}  removed', lst)

# 6. remove: remove the element at specified value
lst = [2, 4, 34, 100, [2, 43]]
rm = [2, 34, 100]
for i in rm:
    lst.remove(i)
print(lst)


# index(): return the index of element
lst = [2, 4, 34, 100, [2, 43]]
re = lst.index(2)
print(re)  # 0

# count() : count the frequency of the element
lst = [2, 4, 34, 100, [2, 43], 100, 2]
re = lst.count(100)
print(re)  # 2

# 9. sort : sort the list
# example 1
lst = [2, 4, 34, 10, 100, 2, 0 ]
print(f'before sorting {lst}')
lst.sort()
print(f'after sorting {lst}')

# example 2
lst = ['ravi', 'ram', 'akshay', 'akhil']
print(f'before sorting {lst}')
lst.sort(reverse=True)
print(f'after sorting {lst}')


# 10. reverse()
lst = [2, 4, 100, 'Hi']
lst.reverse()
# re = lst[::-1]
print(lst)

# 11. copy: return the copy of the list
lst1 = [2, 4, 43, 100]
lst2 = lst1.copy()  # list class method copy
# lst2 = lst1[:] alternate method slicing
lst2.append(100)
print('lst1', lst1)  # lst1 [2, 4, 43, 100]
print('lst2', lst2)  # lst2 [2, 4, 43, 100, 100]


# sort the list with item length
# def apna_fun(x):
#     return  x[-1]

lst = ['ravi', 'ram', 'akshay', 'akhil']
lst.sort(key=len)
print(lst)





