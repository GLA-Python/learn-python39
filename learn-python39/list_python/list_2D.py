
# list in a list
# lst = eval(input('enter the list flatten list '))  # user will provide items in the form of list only
lst = list(map(int, input().split()))  # space separated items
r, c = map(int, input('enter the matrix dimension RXC: ').split('X'))

# output [[2, 5, 6], [34, 53, 65]]
M = []
l = []
count = 0
if r * c == len(lst):
    for i in lst:
        l.append(i)
        count += 1
        if c == count:
            M.append(l)
            l = []
            count = 0
    for i in M:
        for k in i:
            print(k, end=' ')
        print()
else:
    print('Invalid Dimension or configuration')




