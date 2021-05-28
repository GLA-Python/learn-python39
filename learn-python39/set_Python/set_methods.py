ls = [3, 4,3, 4]
v = sorted(ls)
print(ls)


# write a python Program to check given list is sorted or not?
# 3 5 65 9 3
# not sorted

# 2 3 65 77
# sorted

lst = list(map(int, input().split()))
print('sorted') if sorted(lst) == lst else print('not sorted')


a = 1
b = 21
v = a if a > 10 else b
# if a > 10:
#     v = a
# else:
#     v = b/.ilkji9







# set()
k = (3, 5, 5)  # tuple

k = {3: 5, 32: 4}
v = k[3]  # 3 is the key return value at key

k = {4, 6, 23, 44, 77}  # set() un-ordered collection
# basic appearance
# theoriticall defination
# value access
# operations
# methods
k = {4, 6, 23, 44, 77}  # unordered
v = k[0]  # TypeError: 'set' object does not support indexing
print(v)

# iteration?  loop
# recursion?

# sequential data(any data structure sequance)
# repetition
# how to access the element of set one by one
k = {4, 6, 23, 44, 77}
for i in k:  # k is set         |list|tuple|dict|string
    print(i)  #


# initialization
# dictionary
d = {}  # dict object
d = dict()

# set()
st = set()  # initialize empty set st
print(st, type(st))
st.add(20)  # add element in a set st
print(st, type(st))
st.clear()  # remove all the elements from set st
print(st, type(st))


# methods
# 1. add(): add the single element in a set

st = {1, 2, 3}
st.add((4, 6))
print(st)  # {1, 2, 3, (4, 6)}

# k = [(1, 3), (2, 90), 'hello', [67, 8]]
# k[-1].append(100)
# print(k)

st = {2, 4, 5, {3, 4}}  # TypeError: unhashable type: 'set'
print(st)

# id()

st = set()  # id will generate
print(st, type(st), id(st))
st.add((2,4))
st.add('sagar')
# st.add({})  # error
# st.add([3, 4])  # error
print(st, type(st), id(st))

# update(): add the multiple items or elements
st = {2, 4}
# st.add([2, 4, 'hi']) # add element as a single entity::: //error
st.update([2, 40, 'hello'])  # add items of sequential data
print(st)


# union(): union between two sets
s1 = {2, 4, 6, 32}
s2 = {2, 3, 6, 8, 32}
# using method
s = s1.union(s2)

# using operators
s = s1 | s2  # union
print(s)



# intersection

s1 = {2, 4, 6, 32}
s2 = {2, 3, 6, 8, 32}
# using method
s = s1.intersection(s2)
print(s)
# using operators
s = s1 & s2  # union
print(s)

# intersection_update()
s1 = {2, 4, 6, 32}
s2 = {2, 3, 6, 8, 32}
# using method
s1.intersection_update(s2)
print(s1)











