"""
Matrix: rectangular array of numbers (mathematical object)
"""
# how to create 2D list or Matrix in Python using list
# validity of matrix
# mathematically operation Addition, subtraction, Multiplication, ect.

# 1D List (1D Array)
'''
Create a 1D list in python using elements given below
2 4 5 6 4 6 4 6 4 6 4 64 6 456 54
'''
# lst = input().split()  # ['2',  '4' ... '456',  '54']
# row data to list data
lst = list(map(int, input().split()))  # [ 2, 4, ... 456, 54]
# lst = [2, 4 ,5 ,76, 7, 6]
print(lst)


# 1D array with number of elements
N = int(input('enter the number of elements '))
lst = [0] * N
print(lst)  # [0, 0, 0, 0, 0 ... 0]  Dim 1 X N


# Matrix (list in a list or list of list )
'''
lst = [[2, 5], [4, 6], [54, 675]]   # 3 X 2

Create a 2D list in python using elements given below with dimension configurationn R X C
2 4 5 6 4 0
3 2
'''
lst = list(map(int, input().split()))  # row data into 1D
r, c = list(map(int, input().split()))

if r * c == len(lst):
    '''
    [[2, 4], [5, 6], [4, 0]]
    2  4
    5  6
    4  0
    '''
    M = []
    ls = []
    count = 0
    for i in lst:
        ls.append(i)
        count += 1
        if count == c:
            M.append(ls)
            ls = []
            count = 0
    # print(M)
    # print M into matrix format
    # [[2, 4], [4, 5], [4, 0]]
    for i in M:
        for j in i:
            print(j, end='  ')
        print()
    # alternate display of matrix
    M = [[13, 57], [20, 45]]
    for i in M:
        print(*i)

else:
    print('Invalid matrix cinfiguration ')


# matrix validity
'''
check the 2D list is matrix or not 
[[3, 54], [22, 32], [4, 65, 10]]

print the element number at position 1, 1

'''
M = eval(input())  # row data into matrix
ln = len(M[0])
for i in M:
    if len(i) != ln:
        print('Not valid matrix')
        break
else:
    print("Valid Matrix")
    print('Element at [1X1]', M[0][0])

# 2D structure
r, c = map(int, input().split())
ls = [[0] * c] * r  # wrong (every row will be copied of next row)
ls = eval(str(ls))
ls = eval(str([[0] * c] * r))  # right




# 2D array (Matrix)
# list of list (list in a list)
lst = [[3, 5, 6], [3, 55, 6], [4, 67, 7]]
'''
Create a 2D list in python using elements given below and 2D configuration (R, C)
2 4 5 6 4 10
3 2
'''
lst = list(map(int, input().split()))  #  row data into 1D array
r, c = list(map(int, input().split()))  # [3,  2]
'''
[[2, 4], [5, 6], [4, 10]]
'''
M = []
ls = []
count = 0
if r * c == len(lst):
    for i in lst:
        ls.append(i)
        count += 1
        if count == c:
            M.append(ls)
            ls = []
            count = 0
    print(M)  # list in 2D format(list in list)
    # display 2D list into matrix format
    # for i in M:  # [[2, 4], [5, 6]]
    #     for j in i:
    #         print(j, end='  ')
    #     print()
    M = [[3, 5], [4, 564]]
    for i in M:  # [[3, 5], [4, 564]]
        print(*i)


    '''
    2  4
    5  6
    '''
else:
    print("Matrix validation failed ")



# check validity of matrix
'''
check given matrix is valid or not 
[[2, 4], [4, 65]]
'''
M = eval(input())  # [[2, 4], [4, 65, 56]]
ln = len(M[0])
for i in M:  # i = [2, 4]
    if ln != len(i):
        print('Not valid Matrix')
        break
else:
    print('Valid Matrix')













