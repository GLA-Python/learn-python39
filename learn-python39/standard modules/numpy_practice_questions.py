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

















