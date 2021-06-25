"""
use for mathematical function
"""


# import math as m

from math import *

num = 18/pi

v = sqrt(num)
fct = factorial(5)

print(v, fct)

v = pow(2, 4)
print(v)









# sqrt(): to calculate the square root of the given number
from math import sqrt
k = sqrt(16)
print(k)


# ceil(): return the smallest integer equal or greater to the number
import math
k = 34.01
v = math.ceil(k)
print(v)


# copysign
x = -3
y = 4
v = math.copysign(y, x)
print(v)




# floor()

num = 23.9202
k = math.floor(num)
print(k)




# log()
import math
v = math.log(19, 10)
print(v)




# byte size calculation
k = 65536
bt = int(math.log(k, 256))+1
print(bt)





#


# square root
from math import *
num = 5
k = sqrt(num)
ans = factorial(num)
print(f'Square root of {num} is {k} and factorial {ans}')




