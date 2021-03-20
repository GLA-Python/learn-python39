ch = input()
if 'A' <= ch <= 'Z':
    print("Upper case alphabet")
elif 'a' <= ch <= 'z':
    print("lower case ")
elif(ch>='0' and ch<='9'):
    print("digit")
else:
    print("special character")
