

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




