"""
concise way to create a list with for loop
for loop inside a list format
"""
# example create the list from 1 to 10
# ls = list(range(1, 11)) # logic 1
# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
ls = []
for i in range(1, 11):
    if i % 2 == 0:
        ls.append(i)
print(ls)
# list comprehension
'''
he basic syntax is
[ expression for item in list if conditional ]
'''
ls = [i for i in range(1, 11)]
print(ls)

# example 2 : with filter
ls = [i for i in range(1, 11) if i % 2 == 0]
print(ls)

# a = print


''''
data type:
    string
    list
    tuple
input()/print()
    format specifiers 
if-else
looping    

'''
