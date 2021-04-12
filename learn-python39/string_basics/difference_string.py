"""
Remove all Characters in Second String which are present in First String
"""
# input section
st1 = input('Enter the first string ')
st2 = input('Enter the second string ')
'''
st1 = 'hello python'
st2 = 'hi cython'
st2 - st1
Output 
ic
'''
st3 = ''
for i in st2:
    if i not in st1:
        st3 += i
print(f'string after filter {st3}')

#
# st1 = 'hello python'
# st2 = 'hi cython'
# print(set(st2) - set(st1))





import re

m = re.finditer('[abc]', 'dtg$b@uagd')
for i in m:
    print(i.start(), i.group())


my_set = {'abcd', 11, 1.1, "11", (1,2)}
print(my_set)