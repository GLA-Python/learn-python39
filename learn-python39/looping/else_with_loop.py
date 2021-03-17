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

