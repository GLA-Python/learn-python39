"""
hackerrank problem
print the prime number upto the range
"""

num = int(input())  # input the number from user
for n in range(2, num+1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=',')


