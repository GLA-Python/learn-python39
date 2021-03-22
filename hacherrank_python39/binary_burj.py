'''
binary burj
   0
   1
  10
  11
 100
 101
 110
 111
1000
1001
1010
'''

num = int(input())
ln = len(bin(num)) - 2
for i in range(num+1):
    # print(f'{{0:>{ln}}}'.format(bin(i)[2:]))
    x = bin(i)[2:]
    li = len(x)
    print(' '*(ln-li)+x)




