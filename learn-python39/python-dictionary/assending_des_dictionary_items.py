"""
Write a Python script to sort (ascending and descending) a dictionary by value.
"""

def khudka_fun(k):  # k = ('amit', 3)
    return k[1]

dct = {'amit': 3, 'raj': 2, 'abhi': 4, 'aastha': 3, 'yash': 0}
itm = list(dct.items())
print(itm)  # before sort  [('amit', 3), ('raj', 2), ('abhi', 4), ('aastha', 3), ('yash', 0)]
itm.sort(key=khudka_fun)  # assending
itm.sort(key=khudka_fun, reverse=True)  # dessending order

print(itm)  # after sort

