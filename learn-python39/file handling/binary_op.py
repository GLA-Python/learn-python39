"""
rb
wb
ab

binary file
mp3
mp4
jpg
png
"""
# binary write operation
# f = open('binary_sample.txt', 'wb')
# h = 'My name is Python Trainer'
# f.write(b'hello, file handling\n')
# f.write(h.encode())
# f.close()


# read file in binary mode
# f = open('binary_sample.txt', 'rb')
# print(f.read().decode())
# f.close()



# seek()
# f.seek('offset', 'origin')
'''
0: beginning
1: current
2: last(end)
'''
# f = open('binary_sample.txt', 'rb')
# # f.read(20)
# # location 20
# f.seek(20, 1)
# data = f.read(2)  # 21, 22
# print(data)
#
# f.seek(-5, 1)
# print(f.tell())
#
# f.close()



# read file last 2 char

f = open('binary_sample.txt', 'rb')

f.seek(10, 0)
print(f.read())

f.close()