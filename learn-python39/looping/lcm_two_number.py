"""
Q1. Write a python program to find the lcm of two number?
"""
# lcm : least common multiple

num1 = int(input('enter the positive integer'))
num2 = int(input('enter the positive integer '))

lcm = num2 if num1 < num2 else num1

while 1:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm += 1
print(f'LCM of two number is {lcm}')



# iteration vs recursion

for i in [2, 4, 54, 65, 6]:
    print(i)


""""
Calculator
Enter the number first number: 
Enter the second number: 

selection the options choice
1> Add
2> Sub
3> Div
4> Mul

enter the choice 1/2/3/4: 

enter Y/N Y for continue and N for exit?

"""

st = '>>>'

