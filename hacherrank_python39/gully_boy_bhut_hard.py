st = input()

node = int(input())
rp = int(input())


print(*(st[node:] + st[:node]).replace(' ', '')*rp)
