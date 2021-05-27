"""
Dictionary (dict): unordered collection of items
Python collection
# # string
# 'dgsdbshbbcbcsdbdsf❤'

1. list(): ordered collection of object
[12, 5.65, 'hello', [343, 43], (4, 645)]
2. tuple(): ordered collection of object
(12, 5.65, 'hello', [343, 43], (4, 645))
-->3. dict()
4. set()



"""

# list revise
info = ['vishnu', 34, 'C', 'GLA University']
print(info, type(info), id(info))
# read
print('Name', info[0])
# write
info[1] = 100  # item assignment
info.append('Ashok')
print(info, type(info), id(info))



# tuple revise
info = ('vishnu', 34, 'C', 'GLA University')
print(info, id(info))

# # read
# print('Name', info[0])
#
# # write
# info[0] = 'Ravi'  #  'tuple' object does not support item assignment
#
info = list(info)
info[1] = 60
info.append('Python Programming')
info = tuple(info)
print(info, id(info))


# dictionary : unordered collection of items and each item is the pair of key and value
# info = ['vishnu', 34, 'C', 'GLA University', 5.76]
# print('name', info[4])


info = {'name': 'vishnu', 'roll number':34, 'section':'C', 'address':'GLA University', 'cpi':5.76}

# print('name', info['name'])
# print('cpi', info['cpi'])

# read operation
print(info['roll number'])

# write operation
info['roll number'] = 100
info['father name'] = 'Rajiv'

print(info)

# initialization of dictionary
# empty collection
# list
lst = []  # list format
lst = list()  # list class constructor  (Python built-in)

# tuple
tpl = ()
tpl = tuple()  # tuple class constructor

# dict empty
dct = {}
dct = dict()  # dict class constructor (python built-in)

# set
st = set()   # set class constructor

# class yash:
#     pass
#
# a = yash()
# print(type(a))

# initialize the dictionary with items
student_info = {'name':'Vishnu', 'section':['C', 'E'], 'roll_number': 36, 'section':'R', 2:343}
print(student_info, type(student_info))


# accessing the element
# key search
print('name', student_info['name'])
print(student_info)


k = ['Ravi', [2, 4, 56], 43]
k = {'name':'Ravi', 'marks':[2, 4, 54, 65], (2, 4): 43}
print(k, type(k))

k = {'car1':'alto', 'car1':'xyz'}
print(k)


# methods in python dictionary (operation with Python)

# 1. clear(): remove all the item from dictionary object
info = {'name': 'Ravi', 'section': 'N', 'subject': 'Python Programming', 'CPI': 56}
print(info, id(info))
info.clear()
print(info, id(info))

# 2. pop(): remove and return the value using key
info = {'name': 'Ravi', 'section': 'N', 'subject': 'Python Programming', 'CPI': 56}
print(info)
k = info.pop('name')
print('pop value', k)
print(info)

# # pop() in list
# lst = [3, 54, 65]
# v = lst.pop(1)
# print(v)
# print(lst)

# 3. popitem(): remove and return the last occurence item(key and value pair) from dictionary
info = {'name': 'Ravi', 'section': 'N', 'subject': 'Python Programming', 'CPI': 56}
v = info.popitem()
print(v)
print(info)

# item deletion
info = {'name': 'Ravi', 'section': 'N', 'subject': 'Python Programming', 'CPI': 56}
del info['section']
print(info)

# deletion statement
# what is deletion statement?
# in deletion statement we use del keyword and use to delete the object
a = (3, 5, 5, 64, 5)
del a
print(a)

# 4. update(): update the dictionary
info = {'name': 'Ravi', 'section': 'N', 'subject': 'Python Programming', 'CPI': 5.6}
up_info = {'section': 'P', 'father': 'Ramesh', 'CPI': 8.4 }
info.update(up_info)
print(info)

# 5. setdefault(): set default value of key and create
info = {'name': 'Ravi', 'section': 'N', 'subject': 'Python Programming', 'CPI': 5.6}
info.setdefault('marks')
info.setdefault('CPI')
print(info)

# 6. fromkeys(): create the dictionary with keys present in a list
k = ['name', 'father', 'mobile', 'address', 'cpi']

dct = dict.fromkeys(k, 'abhi data nhi aaya')

print(dct)















# 1. clear(): clear all the items from the dictionary object
info = {'name':'Vishnu', 'section':'C', 'roll_number': 36, 'address':'GLA'}
print(info, id(info))
info.clear()  # clear all items or empty dictionary
print(info, id(info))

# 2. pop(): remove and return the value item with key
info = {'name':'Vishnu', 'section':'C', 'roll_number': 36, 'address':'GLA'}
d = info.pop('address')
print(d, type(d))
print(info)


# lst = [2, 54, 56]
# k = lst.pop(1)
# print(lst)


# 3. popitem(): remove and return the last item(key and value pair)
info = {'name':'Vishnu', 'section':'C', 'roll_number': 36, 'address':'GLA'}
d = info.popitem()  # pair of key and value in tuple format
print(d, type(d))
print(info)


# item deletion:= use del keyword
info = {'name':'Vishnu', 'section':'C', 'roll_number': 36, 'address':'GLA'}
del info['name']
print(info)


# what is the deletion statement?
# we use del keyword to delete the object
lst = [2, 4, 45, (34, 5)]
del lst[-1]  # example in a list
print(lst)


# 4. update(): update the dictionary with new items and values

info = {'car': 'nano', 'speed': 50, 'model': 2007}
v = {'speed': 70, 'color': 'white'}
info.update(v)
print(info)


# 5. setdefault(): set default value of key and add
info = {'car': 'nano', 'speed': 50}
info.setdefault('color', 'white')
info.setdefault('speed', 0)
info.setdefault('model')
print(info)  # {'car': 'nano', 'speed': 50, 'color': 'white', 'model': None}


# 6. fromkeys(): create new dictionary with keys in a sequential data(list)
# d = {'32': 54}
rc = ['name', 'father', 'roll_num', 'subject']
dct = {}.fromkeys(rc, 'NA')
dct.update({'name': 'Raj'})
print(dct)


# copy(): return the copy of dictionary
info = {'car': 'nano', 'speed': 50, 'color': 'white'}
var = info.copy()
var['color'] = 'black'
var['model'] = 2020
var.clear()
print(info)
print(id(info), id(var))


# get(): return the value using key search

info = {'car': 'nano', 'speed': 50, 'color': 'white'}
# direct key search
# v = info['car']  # return the value of the key if key is present and generate the error or exception of key is not present

# using get method
v = info.get('engine', 'not available')
print(v)


# dict
dct = {(2, 4): 10, (3, 6): 23}

# v = dct[2, 4]

v = dct.get(3, 6)
# t = 3, 5
print(v)


# items(): return the list of items in the form of tuple
info = {'car': 'nano', 'speed': 50, 'color': 'white'}
v = list(info.items())
print(v)


# keys(): return the list of keys

info = {'car': 'nano', 'speed': 50, 'color': 'white'}
v = list(info.keys())
print(v, type(v))

# values(): return the list of values

info = {'car': 'nano', 'speed': 50, 'color': 'white'}
v = list(info.values())
print(v, type(v))



k = [(10, 0), (2, 4), (0, 3)]

# k = [2, 0, 32, 9]
k.sort()
print(k)  # [0, 2, 9, 32]




# copy(): return the copy of dictionary

info1 = {'car': 'nano', 'speed': 50}
info2 = info1.copy()

info2['car'] = 'alto'

print(info1)




# get(): return the value using key

info = {'car': 'nano', 'speed': 50, 'model': 2010}
# direct key search
# v = info['Car']  # return the value of key if key is present and generate the exception(error) KeyError
                # if key is not present in the dictionary
# using get() method
v = info.get('speed', 'ye key hmare pass nhi h')
print(v)


# dict
d = {(3, 4): 2, (4, 7): 5, 3: 100}
# v = d[(3, 4)]
# v = d[3, 4]  # output 2
# v = d.get((3, 4))  # output 2
v = d.get(3, 4)  # output 4
print(v)


# how to read the dictionary from user
# 5
# sub1 23
# sub2 45
# sub3 34
# sub4 50


n = int(input())
dct = {}
for i in range(n):
    # v =  input() # 'sub1 23'
    v = input().split()  # ['sub1', '23']
    dct[v[0]] = eval(v[1])

print(dct)














# update():  update() just update the key with updated dictionary
info = {'name':'Vishnu', 'section':'C', 'roll_number': 36, 'address':'GLA'}
update_info = {'name': 'Vishal', 'father':'Ram Mishra', 'CPI': 6.65}
print(info)
info.update(update_info)
print(info)


# fromkeys(): create a dictionary using keys in a list
lst = ['name', 'student_m', 'cpi', 'address']
info = {}.fromkeys(lst, 'NA')
print(info)



# value() and keys()
info = {'name':'Vishnu', 'section':'C', 'roll_number': 36, 'address':'GLA'}

k = info.keys()
v = info.values()

print(k, type(k))  # dict_keys(['name', 'section', 'roll_number', 'address']) <class 'dict_keys'>
print(v, type(v))  # dict_values(['Vishnu', 'C', 36, 'GLA']) <class 'dict_values'>


# get(): return the value with keys
info = {'name':'Vishnu', 'section':'C', 'roll_number': 36, 'address':'GLA'}

v = info['name']

v = info.get('name', 'NA')
print(v)


# general dictionary question
dct = {(3, 5):50, 30: 65}

# v = dct[3, 5]

v = dct.get(3, 5)
print(v, type(v))
print(dct)


# update(): update the dictionary with other (merge two dictionary)

dct = {'car':'nano', 'speed':10}
v = {'color': 'white', 'speed': 60}
dct.update(v)
print(dct)
print(list(dct.items()))



ls = [2, 4]
k = ls.copy()
k[1] = 100
print(ls)


for i in ls:
    print(i)
    ls[1] = 10
2
10
# print(ls)



# duplicate values
info = {'car1': 'alto', 'car2':'alto'}
v = list(info.values())
for i in info.copy():
    if v.count(info[i]) > 1:
        del info[i]
print(info)

def khudka(k):
    return k[1]

lst = [(1, 3), (10, 0), (2, 2)]
lst.sort(key=khudka)
print(lst)












