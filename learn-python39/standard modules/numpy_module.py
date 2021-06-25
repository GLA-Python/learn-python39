"""
Password Generators
condition for the good password

1.Min length 8 char
2. at least one char from lower-alpha
3. at least one char from upper-alpha
4. at least one digit
5. at least one special char ~!@#$%^&*(()_
"""

# import random
# char_lower = list(map(chr, range(97, 123)))
# char_uper = list(map(chr, range(65, 91)))
# digits = list(map(chr, range(48, 58)))
# special_char = list('!@#$%^&*()_~><{}[]|')
#
# collect_chars = char_uper + char_lower + digits + special_char
# random.shuffle(collect_chars)
# pas = ''.join(random.sample(collect_chars, int(input('enter the length of the password '))))
# print(pas)




# find the square root of the number
# import math as amir
# from math import *
# num = 18/pi
# re = sin(num)
# print(re)
#


# numpy
import numpy
lst = [8, 4, 6, 4]
print('list', lst, lst[0], type(lst[0]))
arr = numpy.array(lst)
print('numpy ndarray', arr, arr[0], type(arr[0]))

# 1. array(): function in numpy module. convert the sequence into the ndarray

# 0 Dimensional Array
import numpy as np
arr = np.array(23)
print(arr, type(arr), arr.ndim)

# example 2: 1-D array
import numpy as np
arr = np.array([3, 4, 6, 23, 5])
print(arr, type(arr), arr.ndim)

# example 3: 1-D array(data type of the elements)
import numpy as np
arr = np.array([200, 130, 127, 23, 257, 255], dtype=numpy.int8)
print(arr, type(arr), arr.ndim)

# example 4: 1-D array
import numpy as np
arr = np.array([2, 4, 53.9, 'hello'], dtype='object')
print(type(arr[-2]))


# example 2-D Array(Matrix)
import numpy as np
arr = np.array([[2, 4, 4], [3, 7, 33]])
print(arr)
print(arr.shape)

arr.shape = 3, 2
print(arr)

print(arr.ndim)




# reshape()
import numpy as np
arr1 = np.array([[2, 4], [3, 3], [2, 10]])
arr2 = arr1.reshape(2, 3)
print('array1', arr1)
print('array2', arr2)



# arange(): create the array with given range
import numpy as np
arr = np.arange(1, 2, .05)
print(arr, type(arr))



# matrix operation
# matrix multiplication
import numpy as np
mat1 = np.array([[2, 4, 5], [2, 4, 6]])
mat2 = np.array([[4, 7], [1, 0], [3, 8]])

if mat1.shape[1] == mat2.shape[0]:
    print(np.dot(mat1, mat2))
else:
    print('Invalid operation')


# elementary multiplication
import numpy as np
mat1 = np.array([[2, 4, 5], [2, 4, 6]])
mat2 = np.array([[4, 7, 1],[ 0, 3, 8]])
print(np.multiply(mat1, mat2))

# print(mat1.__mul__(mat2))






















import numpy
k = numpy.array(89)
print(k, type(k), k.ndim)

# array(): 1-D array
lst = [3, 5, 7, 54]
# print(type(lst[0]))
arr = numpy.array(lst)
arr[0] = 100
print(arr, type(arr[0]), type(arr))
# Type of the element: numpy.int32

# example2: 1-D array (data type of the element)
import numpy as np
arr = np.array([3.0, 5, 4, 3, 'hello'], dtype='object')
print(arr, type(arr[0]), type(arr))


# example3: 1-D array with 8 bit
import numpy as np
arr = np.array([255, 1000, 3, 256, 54, 5], dtype=numpy.int8)
print(arr, type(arr[0]), type(arr))




# array(): 2-D array
import numpy as np
arr = np.array([[3, 5], [4, 6], [4, 2]])
print(arr,arr.ndim, sep='\n')



# print(arr.shape)
# arr.shape = 2, 3
# print(arr)


# 3-D array
import numpy as np
arr = np.array([[[3]]])
print(arr,arr.ndim, sep='\n')










# array() in numpy
# example 1: 0-D array
import numpy as np
arr = np.array(23)
print(arr, type(arr), arr.ndim)


# example 2: 1-D array
import numpy as np
arr = np.array([3, 5, 6, 23])
print(arr, type(arr), arr.ndim)

# example 3: 2-D list
import numpy as np
arr = np.array([[3, 5], [6, 23]])
print(arr, type(arr), arr.ndim)


# Example 4: ndmin in array
import numpy as np
arr = np.array([3, 5, 6, 6], ndmin=5)
print(arr, arr.ndim)


# dtype in array()
import numpy as np
arr = np.array([3, 5, 6, 6], dtype='complex')
print(arr, arr.ndim, type(arr[-1]))


# shape of 2D array(matrix)
import numpy as np
arr = np.array([[2, 3, 5], [4, 6, 2]])
print(arr.shape)
print(arr)
arr.shape = 3, 2
print(arr)

# reshape()
import numpy as np
arr = np.array([[2, 3, 5], [4, 6, 2]])
print(arr)

arr2 = arr.reshape( 3, 2)
print(arr2)


# arange(): generate a array with given range
import numpy as np
arr = np.arange(1, 2.5, .5)
print(arr)




