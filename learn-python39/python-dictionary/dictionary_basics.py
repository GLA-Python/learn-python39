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






