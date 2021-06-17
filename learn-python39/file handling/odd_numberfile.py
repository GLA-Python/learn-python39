"""
WAP to write the odd numbers into a file
"""

start, stop = 1, 45
f = open('oddNumbers.txt', 'w')
p = 0
for i in range(start, stop):
    if i % 2:
        f.write(f"{i}\t")
        p += 1
        if p == 10:
            f.write('\n')
            p = 0

f.close()

# read: read(), readline(), readlines().
# write: write(), writelines(). [file always truncated]
# append: write() mode: [we will add extra data to the existing file]


