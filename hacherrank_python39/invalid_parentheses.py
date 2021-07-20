
st = input()
count = 0

for i in st:
    if i == '(':
        count += 1
    elif i == ')':
        count -= 1
        if count < 0:
            break           

if count == 0:
    print("'True'")
else:
    print("'False'")
            