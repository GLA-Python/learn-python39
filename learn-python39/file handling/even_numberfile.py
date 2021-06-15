"""
WAP to write the even numbers into a file with user given number range???
"""

f = open('even_numberfile.txt', 'w')
start, stop = [1, 101]

# logical part
p = 1
for i in range(start, stop):
    if i % 2 == 0:
        f.write(f"{i}\t")

        p += 1
        if p == 11:
            f.write('\n')
            p = 1
f.close()


# read:  read(), readline(), readlines()
# write: write(), writelines()
# append: write(): file not truncated, we add some extra data to the existing file