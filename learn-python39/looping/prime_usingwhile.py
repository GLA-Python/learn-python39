
num = int(input('Enter the positive integer value '))
i = 2
while i < num:
    if num % i == 0:
        print('Not Prime number ')
        break
else:
    print("Prime number")
