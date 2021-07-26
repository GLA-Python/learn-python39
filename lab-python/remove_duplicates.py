"""
Write a Python function that takes a list and returns a new list with unique elements of the 
first list.
Sample List: [1,2,3,3,3,3,4,5]
Unique List: [1, 2, 3, 4, 5]
"""

lst = eval(input())
# [1,2,3,3,3,3,4,5]

out = []

for i in lst:
    if i not in out:
        out.append(i)


##out = [i for i in lst if ]
        
##[out.append(i) for i in lst if i not in out]        

print('Unique elements list ', out)       


'''  
l2=[]
for i in list(map(eval,input().split())):
    if i not in l2:
        l2.append(i)
print(l2) 
'''
