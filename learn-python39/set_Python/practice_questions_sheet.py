"""
 Write a Python program to remove an item from a set if it is present in the set. HereBothItem
and Set is enter by the User.

"""
# user data is space separated
h = set(map(int, input().split()))
itm = eval(input('enter the item '))

# h.remove(itm)
h.discard(itm)
print(h)




# 2nd
st1 = set('hello')
st2 = set('hi')
re = st1 - st2
# re = st1.difference(st2)
print(re)



# 3rd
st1 = set('hello')
st2 = set('hi')
re = st1 ^ st2
# re = st1.symmetric_difference(st2)
print(re)

