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
n=int(input())
l=len(f"{n:b}")
for i in range (n+1):
    print(f"{i:b}".rjust(l))





