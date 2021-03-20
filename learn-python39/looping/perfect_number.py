# perfect number (sum of all divisor == number)

n=int(input("enter the number"))
s = 0
for i in  range(1,n):
     if(n%i==0):
         s += i
if s == n:
    print("perfect number ")
else:
    print("not a perfect number ")




# prime number
a = 1
b = 100
for num in range(a, b+1):
    c = 0
    for i in range(1, num+1):
        if num % i == 0:
            c += 1

    if c == 2:
        print(num, end=' ')




# else part in for loop

n = int(input('enter the last number '))
for i in range(1, n+1):
    print(i, end=' ')
    print('next>', end='')
    if i > 5:
        break
else:
    print('stop')
print('\nafter loop')




num = int(input('enter the number '))
for i in range(2, num):
    if num % i == 0:
        print('not prime number')
        break
else:
    print('prime number')










