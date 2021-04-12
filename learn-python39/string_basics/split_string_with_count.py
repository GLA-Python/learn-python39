""""
 Divide a string in N equal parts
"""
st = input('Enter the string ')
N = int(input('Enter the number parts '))

'''
input: 
st = python
N  = 3
Output:
['py' 'th' 'on']
'''
lst = [''] * N
count = len(st) // N
j = 0
for p in range(N):
    lst[p] = st[j:j+count]
    j += count

print(lst)
