inp = input()
unit = {'1':'one', '2':'two', '3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
ones = {'10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
tens = {'1':'one','2':'twenty','3':'thirty','4':'fourty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
hun = ' hundred'
thou = ' thousand'

an = []
if eval(inp) != 0:
    inp = inp[::-1]
    for q in range(len(inp)):
        if q==0:
            if unit.get(inp[q],False):
                an.insert(0,(unit[inp[q]]))
        if q==1:
            if tens.get(inp[q],False):
                if tens[inp[q]] == 'one':
                    an.clear()
                    an.append(ones[inp[q]+inp[0]])
                else:
                    an.insert(0,tens[inp[q]])
        if q==2:
            if unit.get(inp[q],False):
                an.insert(0,(unit[inp[q]]+hun))
        if q==3:
            if unit.get(inp[q],False):
                an.insert(0,(unit[inp[q]]+thou))
    print(*an,sep=' ')
else:
    print('zero')