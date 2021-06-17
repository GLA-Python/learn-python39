"""
add some extra data to the file
"""
# 'a': write only permission. file not truncated. if file dosnt exists it will create the file

# read:  read(), readline(), readlines()
# write: write(), writelines()
# append: write(): file not truncated, we add some extra data to the existing file

# f = open('addition.txt')
# f2 = open('copy_addition.txt', 'w')
# f2.write(f.read())
# f2.close()
# f.close()

f = open('addition.txt', 'a')

f.write('\nthird line')

f.close()