
# methods in a list class
# 1. append(): adds an element in the end of the list
# example 1
lst = [2, 4.66, 2+3j, 'hello']  # len 4
print('before append ', lst)
lst.append(10)  # len 5
print('after append', lst)

# example 2
lst = [2, 4.66, 2+3j, 'hello']  # len 4
print('before append ', lst)
lst.append('Python')  # len 5
print('after append', lst)

# example 3
lst = []  # len 0
print('before append ', lst)
lst.append(10)  # len 1
lst.append([2, 4])  # len 2
lst.append('Hi')  # len 3
print('after append', lst)


# 2. extend(): add the list or iterable element in the current list
lst = [1, 3, 5]  # len 3
lst.extend('Hello')  # len 3 + 5 = 8
lst.extend([3])
print(lst)

# 3. insert(): insert the item or element at given position (index)
lst = [2, 5, 50, 'python']
# lst[1] = 100  # item assignment
lst.insert(1, 100) # insert at index 1
print(lst)
# output
# [2, 100, 5, 50, 'python']

# 4. clear(): to clear the list or remove all items from list
lst = [2, 4, 42]
lst.clear()  # clear the list
print(lst)

# pop(): remove the element or item with define index
lst = [1, 3, 'ravi', 100]
re = lst.pop(0)
print(f'element {re} removed ', lst)  # element 1 removed  [3, 'ravi', 100]

# 6. remove(): remove the element with value
lst = [1, 3, 'ravi', 100]
lst.remove('ravi')
print(lst)  # [1, 3, 100]

# example 2: remove multiple items
lst = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i  in [2, 4, 5]:
    lst.remove(i)
print(lst)  # [0, 1, 3, 6, 7, 8, 9]



# 7. count(): count the frequency of the given element
lst = [2, 32, 43, 43, 2, 342, 34]
re = lst.count(2)
print(re)  # 2

lst = [2, 32, 43, 43, 2, 342, 34]
re = lst.count(20)
print(re)  # 0

lst = [2, 32, 43, 43, 2, 342, 34]
re = lst.count('hello')
print(re)  # 0

# 8. index(): return the index of the first element
lst = [2, 43, 'hello', 'Python', [3, 43], 2]
re = lst.index(2)
print(re)  # 1

# 9. sort(): sort the list
lst = [2, 4, 0, 43, 2, 6, 1]
lst.sort(reverse=True)
print(lst)

lst = ['ravi', 'saket', 'amir', 'sagar', 'priya', 'amar']
lst.sort()
print(lst)

# 10. reverse(): reverse the list
lst = ['ravi', 'saket', 'amir', 'sagar', 'priya', 'amar']
lst.reverse()
# lst = lst[::-1]
print(lst)

# copy(): return the copy of list
lst1 = [2, 4, 67]
lst2 = lst1.copy()
lst1[0] = 100
print('list1', lst1)
print('list2', lst2)


# deletion statement
a = 12
print(a)
del a
print(a)

# item deletion with string
st = 'hello'
del st  #  object deletion allowed
del st[0]  # TypeError str' object doesn't support item deletion
print(st)

# list support item deletion and as well as object class deletion
a = 10
lst = [a, 10, 'hi']
del lst[0]  # item deletion
print(lst)


