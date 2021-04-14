"""
distance cover with steps 1, 2, 3, 4, or 5
"""
from math import ceil
cor = int(input('Coordinate of girl friends house\' '))
steps = int((cor + 4) / 5)  # logic 1
steps = (cor + 4) // 5  # logic 2
steps = ceil(cor / 5)  # logic 3

print(steps)