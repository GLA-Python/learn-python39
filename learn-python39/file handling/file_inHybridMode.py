"""
r: read only
w: write only
a: write only with append

rb: read only in binary
wb: write only in Binary
ab: write only with append in Binary mode

r+: read and write mode (file not truncated)
w+: read and write mode(file always truncated)
a+: write and read mode. we can perform read with append
rb+ or r+b : read and write in Binary
wb+ or w+b: read and write in Binary
ab+ or a+b: in Binary mode

"""

f = open('hybridfile.txt', 'wb+')
f.write(b'this is my text in file')

f.seek(0, 0)
data = f.read()
print(data)

# f.write(b'Amir')

f.close()



# 'r+'
# 'Amit my text in file'
f = open('hybridfile.txt', 'rb+')
f.seek(8, 0)
f.write(b'msg ')

f.close()




f = open('filename')

for i in f:
    print(i)




# with statement in file
with open('sampe_file.txt', 'w') as f:
    f.write('first line\n')
    f.write('second line\n')

print(f.closed)

#
with open('sampe_file.txt', 'rb') as f:
    data1 = f.readline()
    print(data1)
    print(f.tell())
    f.seek(0, 0)
    print(f.tell())
    data1 = f.readline()
    f.seek(3, 1)
    print(f.tell())
    print(data1)




# f = open('sampe_file.txt')

# data = f.read().split()
#
# data.sort(key=len)
#
# data[-1]

# w+, wb+ :> write and read permission [file always truncated when open apply]
f = open('addition.txt', 'w+')
f.write('this is my text for preview ')
f.write('\nsecond line')

f.seek(0, 0)
print(f.read())

f.close()


# r+ or rb+: read and write permission[file not truncated]

f = open('addition.txt', 'rb+')
print(f.read())

f.seek(-12, 1)

f.write(b'text at postion -12 from last')

f.seek(0, 0)
f.write(b'THIS')
f.close()


# r+ and rb+ as a append mode
f = open('addition.txt', 'rb+')
f.seek(0, 2)
f.write('\ndata in last')
f.close()


# a+, ab+ : write and read mode with add the data into a file in last
f = open('addition.txt', 'a+')
f.write('hello')
f.seek(0, 0)
data = f.read()
print(data)
f.close()


# read n lines
n = 10
f = open('sample.txt')
for i in range(n):
    print(f.readline())
f.close()
