# lst = list(map(int, input().split()))

ls = list(map(int,input().split()))
_ = 0
for q in range(len(ls)):
    v = ls[q]
    for j in ls[q+1:]:
        _ = v&j if v&j>_ else _
else:
    print(_)
