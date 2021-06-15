"""
WAP to write the prime numbers only into a file numbers between the given range: 1 to 100
"""
# filename: prime.dat/prime.txt

f = open('prime.dat', 'w')
N = range(1, 101)
for i in N:
    count = 0
    for k in range(1, i+1):
        if i % k == 0:
            count += 1

    if count == 2:
        print(i)
        f.write(f'{i}\t')
f.close()



