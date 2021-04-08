'''

'''
# if-else
a = int(input('Enter the number '))
if a < 10:
    print('Number is less than 10')
else:
    print('Number is greater')

# if - elif - else
a = int(input('Enter the number '))
if a < 10:
    print('Number is less than 10')
elif a == 10:
    print('Number is equal to 10')
else:
    print('Number is greater')


# if only statements
uniq = input('enter the password for more details')
print('Name: Ravi')
print('Section: N')
print('Address: GLA University')
if uniq == '1234':
    print('status: single')

# ternary feature in Python if else
x = True
a = 10 if x == True else 20
print(f'Value of a {a} at condition x {x}')

