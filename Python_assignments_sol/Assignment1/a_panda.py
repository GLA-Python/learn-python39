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

# alternate solution
value = str(int(cake_bars.replace(' ', '')))
ways = ceil(int(value, 2) / len(value))
print(ways)

# main solution using list and loop
