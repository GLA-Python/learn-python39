"""
Binary files : mp3, mp4, jpg etc
"""


# writing data into a file with binary mode

# f = open('sample_binary.txt', 'wb')
# st = '\nProgramming'
# f.write(b'My new text from python')
# f.write(st.encode())
# f.close()


# reading binary file
# f = open('sample_binary.txt', 'rb')
# data = f.read()
# print(data.decode())
# f.close()



# read last 5 char of file
# f = open('sample_binary.txt', 'rb')
# f.seek(-5, 2)
# data = f.read()
# print(data)
# f.close()




# append mode with binary file
f = open('sample_binary.txt', 'ab')
f.write(b'\nNew data added')
f.close()





















# writing data into a file in binary mode
# f = open('sample_binary.txt', 'wb')
# var = ' programming'
# f.write(b'hello, Python file')
# f.write(var.encode())
# f.close()

# reading binary files
# f = open('sample_binary.txt', 'rb')
# f.read(20)
# # print(data)
#
# data = f.read(3)  # 21 22 23
# print(f.tell())
# print(data)
#
# f.close()

# seek()
'''
seek(offset, origin)
offset : any integer number 
origin
0: beginning 
1: current
2: last
'''

# f = open('sample_binary.txt', 'rb')
# # f.tell()  # 0
# f.seek(-11, 2)  #
#
# # print(f.read())
#
# f.seek(0, 0)  # cursor location 0
#
# # print(f.tell())
#
# f.seek(10, 1)   # cursor location 10
#
# data = f.read(2)  # cursor location 12[11, 12]
#
# f.seek(-5, 0)
# print(f.tell())
# f.close()







