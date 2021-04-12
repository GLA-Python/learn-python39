"""
 Sort Elements in Lexicographical Order (Dictionary Order)
"""

st = input('Enter the string ')
'''
input:  acfda
output: aacdf 
'''
lst_re = sorted(st)  # return the list of sorted items(char)
st_re = ''.join(lst_re)  # return the string after concat of items with given pattern
print(st_re)