"""
Q1. Write the program to calculate the value of θ if value of n and α given by the user.
θ = nπ + (-1)n α

"""

from math import *
n = eval(input('enter the value of n'))
alpha = eval(input('enter the value of α '))
theta = n*pi + pow(-1, n) * alpha
print(theta)


"""
Q2. Display the value of k 
A = 2 sin {(θ – α)/2} cos {θ + α)/2} 
B = 2 cos {(θ + α)/2} sin {θ - α)/2} 
K = A^2 + B^2 – AB
"""
from math import *
theta = eval(input('enter the value of θ'))
alpha = eval(input('enter the value of alpha '))
A = 2*sin((theta-alpha)/2)*cos((theta+alpha)/2)
B = 2*cos((theta+alpha)/2)*sin((theta-alpha)/2)
K = pow(A, 2) + pow(B, 2) - A*B
print(K)




