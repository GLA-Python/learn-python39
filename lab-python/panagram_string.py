"""
Determine if a sentence is a pangram. A pangram is a sentence using every letter of the 
alphabet at least once. The best known English pangram is:
“The quick brown fox jumps over the lazy dog”.
The alphabet used consists of ASCII letters A to Z, inclusive, and is case insensitive. Input will not 
contain non-ASCII symbols.
"""


st = input().lower()

for i in map(chr, range(97, 123)):
    if i not in st:
        print('Not a Panagram String ')
        break
else:
    print('Panagram String ')
        


# using set
st = set(input())
alpha_set = set(map(chr, range(97, 123)))

if not len(alpha_set - st):
    print('Panagram ')
else:
    print('Not Panagram ')
    
