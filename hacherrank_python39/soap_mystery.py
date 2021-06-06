N = int(input())
lst = list(map(int, input().split()))
for _ in range(int(input())):
    count = 0
    n = int(input())
    for i in lst:
        if i < n:
            count += 1
    print(count)