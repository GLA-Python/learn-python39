name1 = input()
name2 = input()

name1choice = input()
name2choice = input()
w = name2
if name1choice == 'Paper':
    if name2choice == 'Rock':
        w = name1
elif name1choice == 'Rock':
    if name2choice == 'Scissor':
        w = name1
else:
    if name2choice == 'Paper':
        w = name1

print(f'{w} Win')