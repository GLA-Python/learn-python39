N = int(input())
st = input()

for i in range(int(input())):
    node = int(input())
    print(st.count(st[node-1], 0, node-1))
