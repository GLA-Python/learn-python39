li=''
while li[-1]!='}':
    li+=input()
d=eval(li)
s=set()
l=list(d.values())
for i in d:
    for j in d[i]:
        s.add(j)
l2=sorted(list(s))
c=0
while len(l)!=0:
    l3=[]
    for i in l:
        for j in i:
            l3.append(j)
    d2={i:l3.count(i) for i in l2}
    m=max(d2,key=d2.get)
    l4=[]
    for i in l:
        if m not in i:
            l4.append(i)
    l=l4
    c+=1
print(c)
