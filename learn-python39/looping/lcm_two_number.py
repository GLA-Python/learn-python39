"""
Q1. Write a python program to find the lcm of two number?
"""
# lcm : least common multiple

num1 = int(input('enter the positive integer'))
num2 = int(input('enter the positive integer '))

lcm = num2 if num1 < num2 else num1

while 1:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += 1
print(f'LCM of two number is {lcm}')

