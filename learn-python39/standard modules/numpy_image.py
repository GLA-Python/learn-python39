# import cv2
# k = cv2.VideoCapture(0)
# while 1:
#     flag, img = k.read()
#     img[100:140,:] = 255
#     cv2.imshow('image', img)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cv2.destroyAllWindows()


# import numpy as np
# import matplotlib.pyplot as plt
# board = np.zeros([120, 120, 3])
# for i in range(0, 121, 20):
#     board[i+10:i+20, :] = 1
#     board[:, i+10:i+20] = 1
#
# plt.imshow(board)
#
# plt.show()

# from PIL import Image
# import numpy as np
#
# w, h = 512, 512
# data = np.zeros((h, w, 3), dtype=np.uint8)
# data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
# img = Image.fromarray(data, 'RGB')
# # img.save('my.png')
# img.show()



# numpy array()

import numpy as np

arr = np.array([[3, 5, 5], [4, 7, 0]])

print(arr.ndim)

print(arr.shape)

arr.shape = 3, 2
print(arr)


# reshape()
import numpy as np
arr = np.array([[3, 5, 5], [4, 7, 0]], ndmin=3)
# arr2 = arr.reshape([3, 2])
print(arr)


# arange()
import matplotlib.pyplot as plt
import numpy as np
k = np.arange(0, 10, .25)
value = np.sin(k)
value2 = np.cos(k)

plt.plot(k, value, linewidth=5)
plt.plot(k, value2, linewidth=5)

plt.show()




# array sum
import numpy as np
lst = [[2, 4, 54], [6, 32, 2]]
arr = np.array(lst)
print(arr, end='\n\n')
s = np.max(arr, axis=0)
print(s)



# linspace
arr = np.linspace(2, 4, 19)
print(arr)




















#
# import cv2
# import matplotlib.pyplot as plt
#
# cam = cv2.VideoCapture()
#
# while 1:
#     flag, img = cam.read()
#     cv2.imshow('My image', img)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
# cv2.destroyAllWindows()


























# matrix multiplication

mat1 = np.arange(12).reshape(3, 4)
mat2 = np.arange(12).reshape(4, 3)

res = np.dot(mat1, mat2)
print(res)













# sin-cosine in numpy
import numpy as np
import matplotlib.pyplot as plt

x_axis = np.arange(0, 11, .25)
y_data1 = np.sin(x_axis)
y_data2 = np.cos(x_axis)

plt.plot(x_axis, y_data1, color='yellow', linewidth=4)
plt.plot(x_axis, y_data2, color='green', linewidth=10)

plt.show()




# matrix behaviour
import numpy as np

mat1 = np.arange(12).reshape(3, 4)
mat2 = np.arange(4, 16).reshape(3, 4)
#elementry multiplication
print(np.multiply(mat1, mat2))
mat2 = np.transpose(mat2)
#dot multiplication
print(np.dot(mat1, mat2))

print(mat1)
print(mat2)



# array as image

import numpy as np
import matplotlib.pyplot as plt

mat = np.zeros([100, 100, 3])

for i in range(0, 100, 20):
    mat[i+10:i+20, :] = 1
    mat[:, i+10:i+20] = 1

plt.imshow(mat)

plt.show()


# sum
import numpy as np

arr = np.arange(12).reshape(3, 4)

re = np.sum(arr, axis=1)
print(re)


# linspace

arr = np.linspace(1, 4, 100)
print(arr)


# Q1. Write a Python program to create an array using numpy of
#       all the even integers from 1 to 100.
import numpy as np
start = 1
stop = 100
arr = np.arange(start+1, stop+1, 2)
print(arr, type(arr))

# Q2. Write a program to test whether none of the elements
#   of a given numpy array is more than 100.

import numpy as np
arr = map(eval, input('enter the space separated elements of the array').split())
# arr = np.array(arr)
result = True
# logic here
for i in arr:
    if i > 100:
        result = False
        break

if result:
    print('Test pass,none of the elements of a given numpy array is more than 100 ')
else:
    print(f'Test failed, more than 100 value found {i}')





# Q3 Write a Python program to create an array with the integer values and
#       determine the size of the memory occupied by the array. Comparison with list also
import sys
lst =  [200, 256, 6, 4, 78]
k = sys.getsizeof(lst)
print(k, 'bytes list')

import numpy as np
arr = np.array(lst, dtype=np.int8)

print(arr, arr.size*arr.itemsize, 'bytes array')



# 4. Write a NumPy program to create a NxN identity matrix.
#   N is user entered positive Integer.
import numpy as np
N = int(input('enter the positive integer '))
mat = np.eye(N)
print(mat)


# 5. Write a Python program to remove all the numbers in a given array which is
#   equal and greater to a given number

import numpy as np
N = int(input('Enter the number '))
arr = np.array([2, 54, 66, 2, 8, 90])
print(list(filter(lambda x: x <= N, arr)))





# c100





# # ploting
#
# import numpy as np
# import matplotlib.pyplot as plt
# arr_xaxis = np.arange(0,10,.25 )
#
# arr_ydata = np.sin(arr_xaxis)
# arr_ydata2 = np.cos(arr_xaxis)
#
# plt.plot(arr_xaxis, arr_ydata, color='green', linewidth=10, )
# plt.plot(arr_xaxis, arr_ydata2, color='pink')
# plt.show()


# invert
# import numpy as np
#
# h1 = np.arange(6).reshape([2, 3])
# h2 = np.arange(6).reshape([2, 3])
# print(np.divide(h1, h2))

# print(np.invert(h))
# print(np.transpose(h))