"""
number of ways to break the cake
input
3
0 1 0
Output
1
"""
from math import ceil
pieces = int(input('Enter the number of pieces '))
cake_bars = input(f'Enter the {pieces} integers ')

# alternate solution: some cases failed
value = str(int(cake_bars.replace(' ', '')))
ways = ceil(int(value, 2) / len(value))
print(ways)

# main solution using list and loop
cake_bars = list(map(int, cake_bars.split()))
count = 0
sum = 1
i = 0
while i < pieces:
    count = 0
    if cake_bars[i]:
        i += 1
        while i < pieces:
            if cake_bars[i]:
                sum *= count + 1
                break
            count += 1
            i += 1
            # print(count)
        else:
            if cake_bars[i-1]:
                sum *= count+1
    else:
        i += 1
print(sum)