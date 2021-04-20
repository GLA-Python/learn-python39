"""
short circuit evaluation with logical operators
"""
'''
False Value
0, False, [], (), set(), '', {}, None

'''

re = 0 and 1
re = 0 or 1
print(re)

if [] and 'hello':
    print('List with some data ')
else:
    print('Empty list ')

# or example
re = 'Hi' or 10 + 'hello'
print(re)

re = 10 > 20 or 'hello' or 'Python'
print(re)  # 'hello'


# and
re = '' and 10 + 'hello'
print(re)  # '' empty string



# mix example

re = 10 == 10.0 and list() or 2 < 3 and not 'python'
print(re, type(re))  # False class<'bool'>







