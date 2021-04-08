ch = input()

# k = 'hello 😒 ❤'
# print(k[-3])

if 'A' <= ch <= 'Z':
    print('Upper case alphabet')
elif 'a' <= ch <= 'z':
    print('lower case alphabet')
elif '0' <= ch <= '9':
    print('digits')
else:
    print('Special Characters ')
