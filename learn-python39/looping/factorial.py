# factorial of given number
n = int(input('enter the number '))
fact = 1
for i in range(n, 0, -1):
    fact = fact * i
print('Factorial is ', fact)
