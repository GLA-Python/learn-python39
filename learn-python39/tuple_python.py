"""
Tuple: we can create the tuple by placing the objects within parenthesis
tuple is immutable in nature
tuples are fixed object values
"""
# examples
lst = [2, 4, 5, 6, 'hello']  # list in Python
tpl = (2, 5, 7, 76, 86, 'hello', (4, 54), [43, 54, 5])  # tuple in Python
# both list and tuple is ordered collections ion Python

# initialization of tuple
# empty collection
tpl = ()   # tuple format
tpl = tuple()  # tuple class constructor
print(tpl, type(tpl))   # output () class<'tuple'>


# initialize with objects
tpl1 = (2, 4, 5, 'hello') # tuple
tpl2 =  2, 4, 5, 'hello'  # tuple
print(tpl2)  # (2, 4, 5, 'hello')

# single value tuple
tpl1 = (10, )
tpl2 = 10,
tpl3 = ('hello')   # not a tuple

# concat
tp1 = 12, 4
tp2 = (2, 6)
tp = tp1 + tp2
print(tp, type(tp))  # (12, 4, 2, 6) class<'tuple'>


# accessing the elements or values
# indexing
# slicing
tp = ('hello', 'python', 43, 54, 12+4j)
re = tp[7]  # index error
re = tp[-1]  # last element complex number
print(re, type(re))

# slicing
# example 1
tp = ('hello', 'python', 43, 54, 12+4j)
re = tp[1:]  # range 1 2 3 4
print(re, type(re))  # ('python', 43, 54, (12+4j) ) class<'tuple'>

#example 2
tp = ('hello', 'python', 43, 54, 12+4j)
re = tp[100:200]  # range 100 ... 199
print(re, type(re))  # () class<'tuple'>


# string
st = 'hello'
re = st[1:3]  # range 1, 2
print(re)  # el


# list in tuple
tp = (4, 453, 43, 53, 34)

# item assignment
tp[0] = 100 # tuple dosnt support the item assignment

# list in tuple
tp = (23, 'hello', 3.65, [3, 65, 67, 7])
print(id(tp[-1]))
tp[-1].clear()
# del tp[-1]  # item deletion not allowed
print(id(tp[-1]))
tp[3].append(100)
tp[-1][0] = 'Hello'
print(tp)  # output (23, 'hello', 3.65, ['hello'])


# tuple in a list
lst = [2, 5, (3, 5), [4, 54]]
lst[2][0]  = 100
print(lst)


# lst = [2, 4, 5, 564, 5, [33, 4], (4, 54)]
# del lst[-1]
# print(lst)



# tuple generator
tp = (i for i in range(3))
# 1. using next()
# 2. collection cast tuple, list
# 3. for loop

print(next(tp))  # 0
for i in tp:
    print(i)  # 1
    print(list(tp))  # [2]
print(list(tp))  # []



# lst1 = [3, 54, 6]
# # lst2 = [10, 0, 0]
# #
# # print(list(zip(lst1, lst2)))
# #
# # for i, j in zip(lst1, lst2):


#
lst = [2, 4, 5, 6]
lst[:] = ''
print(lst)




