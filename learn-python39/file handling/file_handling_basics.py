"""
file handling: reading and writing operation with local file.
file : just a information
"""

# standard input/standard output

'''
input(): built-in function for std i/p
print(): built-in function for std o/p
'''

# example 1: sum of two numbers and display the output
import time
num1 = eval(input('enter the first number '))  # standard input
num2 = eval(input('enter the second number '))

out = num1 + num2
x = time.asctime()
print(f'sum of {num1} and {num2} is {out} at {x}')  # standard output

# write the first data into a file
'''
open(filename, mode): built-in function for file handling 

'''
f = open('C:/Users/Amirkhan/Desktop/addition.txt', 'w')

f.write(f'sum of {num1} and {num2} is {out} at {x}')

f.close()
print('\\')

# file management

f = open('table.txt', 'w')
f.write('hello file, this is Python Programming')
f.close()



# wap to display the table 1 to 10 in a file
'''
1   2   3   4..
2   4   6   8..
.
.
'''
f = open('table.txt', 'w')  # open the file in write mode
N = 10
for i in range(1, N+1):
    for j in range(1, N+1):
        print(f'{i*j}\t', end='')
        f.write(str(i*j) + '\t')
    print()
    f.write('\n')
f.close()


# opening the file
'''
k = open(filename, mode)

Mode: 
'r': deafult value, open the time in read mode(operation) . error generate if file not found  
'w': open the file in write mode . it will create the file if file not avaiable 
'a':
'x':
'''

# reading the file
# read(): it will read the entire data of the file from current location
f = open('addition.txt', 'r')
# f.write()  # cant use
data = f.read()  # it will read the entire data of the file
print(data)
f.close()


# read with argv
f = open('addition.txt', 'r')
# data = f.read()
data1 = f.read(10)  # it will the 10 chars only from current
# print(data1)
# print(f.tell())
data2 = f.read(5)
# print(data2)
data = f.read()
print(data)
print(f.tell())
f.close()

# readline(): read the next single line from current
f = open('addition.txt')
data1 = f.readline()
print(len(data1))
f.close()

# readline() with argv
f = open('addition.txt')
data1 = f.readline(49)  # chars limits in a single line 10
data2 = f.readline()
print(data1)
print(data2 )
f.close()


# readlines(): list of lines
f = open('addition.txt', 'rb')
data = f.readlines()
print(data)
f.close()
# f = open('filename', 'mode')
'''
1. read(): read all chars in a file  
2. readline(): single line string
3. readlines(): list of lines 
'''


# iterator behaviour of file object:
# with next()
# # with loop()

f = open('addition.txt')
# using next() built-in function

while 1:
    k = next(f, 0)
    if k != 0:
        print(k)
    else:
        break
f.close()


# # using for loop
f = open('addition.txt')
# using for loop function
for line in f: # line = 'hello...'
    k = next(f)
    print(k)

f.close()



# write operation:
# 1. write()
# 2. writelines()
"'w': open the file in write mode. create the file if file not exist"
#
f = open('sample.txt', 'w')
if not f.closed:
    print('file succesfully opened')
    f.write('this is a \nsample text for sample file')
    f.write('\nusing python programming')
    f.close()
    if f.closed:
        print('file successfully saved')
else:
    print('file not opened')



# writelines()

f = open('sample.txt', 'w')

kh = ['first line\n', 'second line\n', 'third line\n']

f.writelines(kh)

f.close()








# standard input/ standard output
'''
input(): built-in for std i/p
print(): built-in for std o/p 
'''
'''
# example 1: sum of two number and display the output
import time
num1 = eval(input('enter the first number '))  # standard input
num2 = eval(input('enter the second number '))
out = num1 + num2
x = time.asctime()
print(f'sum of {num1} and {num2}  is {out} at {x}')  # standard output

# write data in local file
'''
#file object = open(filename, mode)
'''
f = open('C:\\Users\\Amirkhan\\Desktop\\record_sum.txt', 'w')
f.write(f'sum of {num1} and {num2}  is {out} at {x}')
f.close()
'''

# file
# f = open('table.dat', 'w')
# f.write('this is my file created by Python Programming')
# f.write('\nfor the sample file ')
# f.close()


# write a program to print the table 1 to 10 in local file.
'''
1 2 3 4 5
2 4 6 8 10...
4 8 12 .....
# 
# '''
# f = open('table.txt', 'w')
# N = 10
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         print(f'{i*j}', end='\t')
#         f.write(f'{i*j}\t')
#     print()
#     f.write('\n')
# f.close()


#
#
# # example sum of two number and print the output with comment
# import time
# num1 = eval(input('enter the first number '))  # standard input
# num2 = eval(input('enter the second number '))
# c = num1 + num2
# x = time.asctime()
# print(f'sum of {num1} and {num2} is {c} at time {x}')
#
#

#
# # open(): built-in function
# '''
# #use of open('filename', 'mode') function
#
# '''
#
#
# f = open('C:\\Users\\Amirkhan\\Desktop\\sum_record.txt', 'w')
#
# f.write(f'sum of {num1} and {num2} is {c} at time {x}')
#
# f.close()
# '''
#
# # local file
# #
# # f = open('sum_record.txt', 'w')
# # f.write('Hello file, created by Python\n')
# # f.write('this is my first time to write \nsomething in file')
# # f.close()
#
#
# # write the number table upto 10 into a file name is table.txt
# '''
# 1 2 ...
# 2 4
# 3 6
# 4 8
# 5 10
# 6 12
# 7 14
# 8 16
# 9 18
# 10 20
#
# '''
#
# f = open('table.txt', 'w')
# N = 10
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         f.write(str(i*j) + '\t')
#     f.write('\n')
#
# f.close()
#
#
#
#
#
#
