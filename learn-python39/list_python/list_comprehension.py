"""
concise way to create a list with for loop
for loop inside a list format
"""

lst = []
for i in range(20):
    if i % 2 == 0:
        lst.append(i)
print(lst)


# [ expression for item in list if conditional ]
lst = [i for i in range(20) if i % 2 == 0 ]  # i = 0
print(lst)  # [0, 2, 4, 6, 8, 10...18]


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

# example 2 :  filter the given list with even values
lst = [2, 4, 2, 42 ,4 ,676, 87, 3, 65, 65, 6,5, 64]
lst1 = [i for i in lst if i % 2 != 0]
print(lst1)


# Example 3: modify the list elements to float
lst1 = [2, 4, 6, 76, 23]


lst = [float(i) for i in lst1]

# Output:
lst = [2.0, 4.0, 6.0, 76.0, 23.0]






# all the elements of list is integer
lst2 = [float(i) for i in lst1]  # using list comprehension
lst2 = list(map(float, lst1))  # alternate using map function
print(lst2)  # [2.0, 4.0, 6.0, 76.0, 23.0]



arr = eval(input())
r, c = map(int, input().split('x'))
M = []
count = 0
ls = []
if r*c == len(arr):
    for i in arr:
        ls.append(i)
        count += 1
        if c == count:
            M.append(ls)
            count = 0
            ls = []
    for i in M:
        print(*i)
else:
    print('invalid')



s = eval(input())
for i in s:
    s.remove(i) if not len(i) else None
print(s)





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
