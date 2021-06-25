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
import numpy as np
k = np.arange(0, 10, 2.5)
print(list(k))



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