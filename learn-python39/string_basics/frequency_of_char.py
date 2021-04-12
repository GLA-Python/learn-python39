"""
 Find the Frequency of Characters in a String
"""

st = input('Enter the string ')
'''
input: hello
output:
h: 1
e: 1
l: 2
o: 1
'''
reg = ''
for i in st:
    if i not in reg:
        reg += i
        print(f'{i}: {st.count(i)}')

