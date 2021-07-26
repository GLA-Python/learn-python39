"""
THE WAR

"""


r, c = map(int, input().split(' x '))
count = 0
for i in range(1, r+1):
    for j in range(1, c+1):
        if (i + j) % 2:
            count += 1
print(count)            
