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



# methods in python dictionary

# 1. clear(): clear all the items
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













