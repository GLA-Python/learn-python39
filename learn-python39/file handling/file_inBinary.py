"""
Binary files : mp3, mp4, jpg etc
"""

# example : write data into a binary file
# k = open('binary_sample.txt', 'wb')
#
# info = 'my name is Amir khan'
#
# k.write(info.encode())
#
# k.close()


# read binary data
# f = open('binary_sample.txt', 'rb')
# data = f.read().decode()
# print(data)
# f.close()


# seek

f = open('binary_sample.txt', 'rb')

'''
seek(offset, origin)
0: beginning
1: current
2: last
'''
f.seek(4, 0)  # 4

print(f.read()) # 5

f.seek(-3, 1)  # 2
print(f.tell())

f.close()







