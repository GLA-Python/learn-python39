"""
remove the char from given string except alphabet
"""
# input section
st = input('Enter the string ')
st2 = ''
# logic section
for i in st:
    if i.isalpha():
        st2 += i
# output section
print(f'filter string with alphabet only {st2}')