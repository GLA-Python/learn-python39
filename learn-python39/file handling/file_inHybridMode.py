"""
r: read only
w: write only
a: write only with append

rb: read only in binary
wb: write only in Binary
ab: write only with append in Binary mode

r+: read and write mode (file not truncated)
w+: read and write mode(file truncated)
a+: write and read mode. we can perform read with append
rb+ or r+b : read and write in Binary
wb+ or w+b: read and write in Binary
ab+ or a+b: in Binary mode

"""

# f = open('hybridfile.txt', 'wb+')
# f.write(b'this is my text in file')
#
# f.seek(0, 0)
# data = f.read()
# print(data)
#
# # f.write(b'Amir')
#
# f.close()



# 'r+'
# 'Amit my text in file'
# f = open('hybridfile.txt', 'rb+')
# f.seek(8, 0)
# f.write(b'msg ')
#
# f.close()


'''
monisha
tanishq
'''
#
# f = open('filename')
#
# for i in f:
#     print(i)




# with statement in file
with open('sampe_file.txt', 'w') as f:
    f.write('first line\n')
    f.write('second line\n')

print(f.closed)


with open('sampe_file.txt') as f:
    print(f.read())

print(f.closed)







