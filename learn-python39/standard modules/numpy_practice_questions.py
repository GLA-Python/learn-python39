"""
Q1. Write a Python program to create an array using numpy of all the even
    integers from 1 to 100
"""
import numpy as np
start = 1
end = 100
arr = np.arange(start+1, end+1, 2)
print(arr, type(arr))


"""
Q2. Write a program to test whether none of the elements of a given 
    numpy array is more than 100. 
"""
import numpy as np
arr = np.array([2, 54, 78, 34, 98])
re = True

# logic here
for i in arr:
    if i > 100:
        re = False
        break
if re:
    print('Test case passed, none of the elements of a given numpy array is more than 100')
else:
    print('Test failed, more than 100 value found')



"""
Q3. Write a Python program to create an array with the integer values and 
    determine the size of the memory occupied by the array. Comparison with list also
"""
import sys
import numpy as np
arr_collect = list(map(eval, input('enter the space separated integer values').split()))
arr = np.array(arr_collect)
# size of array
print(arr.size*arr.itemsize, 'bytes in numpy array')
print(sys.getsizeof(arr_collect), 'bytes in list array')



"""
Q4.Write a NumPy program to create a NxN identity matrix. 
        N is user entered positive Integer.
"""
import numpy as np
N = int(input('Enter the positive integer '))
mat = np.eye(N)
print(mat)


"""
Q5. 5. Write a Python program to remove all the numbers in a 
    given array which is equal and greater to a given number
"""

import numpy as np
lst = list(map(eval, input('enter the space separated integer values').split()))
N = int(input('enter the number for filter '))
list_array = list(filter(lambda x: x < N, lst))
print(np.array(list_array))















"""
Q1. Write a Python program to create an array using numpy of all the 
    even integers from 1 to 100.
"""
import numpy as np
start = 1
stop = 100
se = np.arange(start+1, stop+1, 2)
print(se, type(se))



"""
Q2. Write a program to test whether none of the elements 
    of a given numpy array is more than 100. 
"""

import numpy as np
arr = np.array([2, 54, 66, 44, 705])
# re = True
# logic here
# for i in arr:
#     if i > 100:
#         re = False
#         break
re = True if np.max(arr) < 100 else False
if re:
    print('Test pass, none of the elements of a given numpy array is more than 100')
else:
    print('Test failed, more than 100 value found ')


"""
Q3. Write a Python program to create an array with the integer values and 
    determine the size of the memory occupied by the array. Comparison with list also.
"""
import numpy as np
import sys
k = list(map(int, input('enter the space separated integer values').split()))
arr = np.array(k)
print(arr, arr.size*arr.itemsize, 'bytes in array')
lst = [3, 54, 504, 43, 10]
print(k, sys.getsizeof(k), 'bytes in list format')

"""
Q4. Write a NumPy program to create a NxN identity matrix. 
    N is user entered positive Integer.
"""
import numpy as np
N = int(input('enter the positive integer '))
mat = np.eye(N)
print(mat)





# temp solution
import numpy as np
lst = [[3, 4, 6], [3, 4, 1], [20, 3, 10]]
# lst = [[3, 5, 2]]
arr = np.array(lst)
mx = np.max(arr, axis=1)
# print(mx)

for c, i in enumerate(lst):
    i[i.index(mx[c])] = i[-1]
    i[-1] = mx[c]

print(np.array(lst))




import numpy as np
lst = list(map(int, input('enter the space separated integer values').split()))
r, c = map(int, input().split())
mat = np.array(lst).reshape(r, c)
print(mat)













