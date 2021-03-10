h = 10  # height
r = 5  # radius
F = 15  # flow rate
t = eval(input('Enter the time '))
Vwtr = F*t
Vtank = 3.14*r**2*h

if Vwtr > Vtank:
    print("Over flow condition")
    print("Volume", Vwtr - Vtank)
elif Vwtr == Vtank:
    print("Tank full")
else:
    print("Under flow Condition")
    ht = Vwtr / (3.14*r**2)
    hr = h - ht
    print(f'filled height {ht} and remaining height {hr}')
