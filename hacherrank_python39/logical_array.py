# lst = list(map(int, input().split()))

l=list(map(int,input().split()))
m=[]
l1=l.copy()
if(len(l)>0):
    for i in range(len(l)):
        l1.pop(i)
        for j in l1:
            m1=l[i]&j
            m.append(m1)
        l1.insert(i,l[i])
print(max(m)) 