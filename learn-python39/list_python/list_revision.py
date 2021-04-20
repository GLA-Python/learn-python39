roll_number1 = [10, 23, 43, 22, 20, 'ravi', 'saket']

# indexing: get the single element
k = roll_number1[-8]  # IndexError: index out of range
print(k, type(k))

# slicing : sublist from list
roll_number1 = [10, 23, 43, 22, 20, 'ravi', 'saket']
k = roll_number1[-1:4:-1]  #  6 5 4
print(k, type(k))
