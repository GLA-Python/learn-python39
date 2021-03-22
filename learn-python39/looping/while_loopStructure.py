# while loop

# while expression:
#     # statements
# else:  # optional
#     # statements


num = int(input('enter the positive integer '))
fact = 1
while num > 0:
    fact *= num
    num -= 1
print(f'factorial of given number is {fact}')