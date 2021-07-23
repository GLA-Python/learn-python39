row = int(input('enter the number of rows '))
mid = int(input('Mid line'))

# # hollow triangle using single expression 
# for i in range(1, row+1):
#     print(' ' * (row - i) + '*' + ' ' * (2 * i - 3) + '*' * (i != 1), end='\n' + '*' * (i == row and row * 2-1))


# solution 2nd 
k = 0
for i in range(1, row+1):
    print(" "*(row-i), end='')
    while k != 2*i-1:
        if k == 0  or k == 2 * i - 2 or i == mid:
            print("*", end='')
        else:
            print(end=' ')    
        k += 1

    k = 0
    print()    
