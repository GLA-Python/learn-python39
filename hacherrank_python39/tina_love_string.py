def erase(st):
    # logic here
    dct = {}
    for i in st:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
    lst = sorted(list(dct.items()), key=lambda x: x[1], reverse=True)
    # print(lst)
    for i in lst:
        if not i[0] == 'a':
            st = st.replace(i[0], '')
            break
    return st
for i in range(int(input())):
    st = input()
    while not st.count('a') > len(st) // 2:
        st = erase(st)
    else:
        print(len(st))