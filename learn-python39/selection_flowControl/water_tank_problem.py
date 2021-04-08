h = 10
r = 5
F = 15
T = int(input("Enter the time in min"))
vtank = 3.14 * r ** 2 * h
vwtr = F * T
if vwtr > vtank:
    print("over flow")
    print('volume of', vwtr - vtank)
elif vwtr == vtank:
    print("tank full")
else:
    print("not full")
    ht = vwtr / (3.14*r**2)
    hr = h - ht
    print(f'filled height {ht}\nremaining height {hr}')