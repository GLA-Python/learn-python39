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
w = len(bin(num)[2:])
for i in range(num+1):
    print(f'{{0:>{w}}}'.format(bin(i)[2:]))
    # x = bin(i)[2:]
    # print(' '*(w-len(x))+x)
      
      
n=int(input())
for i in range(n+1):
    b=bin(i).replace("0b","") 
    for j in range(len(bin(n).replace("0b",'')) - len(b)):
        print(" ",end='')
    print(b) 







