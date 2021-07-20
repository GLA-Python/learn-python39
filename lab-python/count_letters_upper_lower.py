""" Python function that accepts a string and calculate the number of uppercase letters and 
lowercase letters.
Sample String: 'The quick Brow Fox'
Expected Output:
No. of Upper case characters: 3
No. of Lower case Characters: 12
"""


st = input('Enter the string ')

count_upper = 0
count_lower = 0
for i in st:
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower += 1

print(f"User string {st}")
print(f"Number of upper case letters {count_upper}")
print(f"Number of lower case letters {count_lower}")
