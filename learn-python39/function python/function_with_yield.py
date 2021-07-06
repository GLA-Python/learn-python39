"""
we use yield when we need to iterate over the sequence and we dont want to store entire sequence in a memory.
Yield used in Python generator(generator like a normal function but whenever it needs the value it does)
"""
# operations with number


def opera(num):
    return num * 2, num * 3, num * 4  # return statement close the execution of the function with return value in memory
    print('after return')
    print(vag)


a = 2
x = opera(a)
print(x)

# with yield


def opera(num):
    yield num * 2  # add value (num*2) to generator
    yield num * 3  # add value to generator
    yield num * 4  # add value to generator
    # yield doesnt close the execution
    print('after yield')
    print(3)
    yield 20
    print('in the end')
a
a = 2
x = opera(a)
print(x)

b=np.array([[1,2,3,4],[5,6,7,8],[10,11,12,13]])
b[2,1]

# Mark the right output from the below options

# Mark the right output from the below options

