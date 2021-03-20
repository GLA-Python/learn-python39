num1, num2 = map(int, input().split())
if num1 ^ num2  == num1 + num2:
    print("'Valentine Match'")
else:
    print(None)
