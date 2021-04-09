"""
find whether given number is armstrong or not
1. using for loop
2. using while loop
"""

# input section
num = input('Enter the positive integer ')
s = 0  # to collect the sum of the power of each digit raise to its length

#logic section
x = len(num)
for ch in num:
    s += int(ch)**x

# output section
if s == int(num):
    print(f'Number {num} is Armstrong')
else:
    print(f'Number {num} is not Armstrong')

