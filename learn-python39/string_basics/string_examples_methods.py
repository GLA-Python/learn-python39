# how to initialize a string
a = ''  # empty String using string format
a = str()  # empty string using string class constructor
print(a)  # output:- ''

# method
# capitalize() capitalize the first letter
st = 'hello world'
re = st.capitalize()
print(re, type(re))  # output Hello world <class str>

# title()
st = 'hello world'
re = st.title()
print(re, type(re))  # Output Hello World

# upper()
st = 'hello world 123@'
re = st.upper()
print(re)  # Output HELLO WORLD 123@
# lower()
st = 'hello world 123@'
re = st.lower()
print(re)  # Output hello world 123@

# split()
st = 'he\tllo    pyth\non  programming'
re = st.split()
print(re, type(re))


ls = input().split()
# a = int(ls[0])
# b = int(ls[1])
# c = int(ls[2])

ls = list(map(int, ls))
a, b, c = [2, 4, 4]




















