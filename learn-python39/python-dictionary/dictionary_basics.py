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
info[1] = 100
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
info = {'name': 'yash', 'roll number':34, 'section':'C', 'address':'GLA University', 'name':'vishnu'}

# read
print(info['section'])
# print(info['father'])

data = info['name']
print(data)


# initialization of dictionary
# empty collection
# list
lst = []  # list format
lst = list()  # list class constructor

# tuple
tpl = ()
tpl = tuple()  # tuple class constructor

# dict
dct = {}
dct = dict()  # dict class constructor

# set
st = set()   # set class constructor

# class yash:
#     pass
#
# a = yash()
# print(type(a))

# initialize the dictionary with items
# lst = [['alto', 'nano'], 70, 'white', 1990]
dct = {'car':['alto', 'nano'], 'speed':70, 'color':'white', 'model':1990}

# accessing the value
# cars = lst[0]
cars = dct['car']







