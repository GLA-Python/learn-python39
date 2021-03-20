# else part with for loop
# optional section
n = int(input('enter the last range '))
for k in range(1, n+1):
    if k > 5:
        break
    print(k, end=' ')
    print('next>', end='')
else:
    print('else part of for loop')
print('\nafter loop')

# prime no. without using third variable
k = int(input('Enter the number '))
for  i in range(2, k):
    if  k%i==0:
        print("Not Prime.")
        break
else:
    print("Prime No.")







n = 8
for i in range(1, n+1):
    if i>5:
        break
    print(i, end=' ')
    print("next>", end='')
else:
    print("else part of for")
print("After for loop")





for i in range(1, 5):
    continue
    print(i, end=' ')
else:
    print('loop completed')











