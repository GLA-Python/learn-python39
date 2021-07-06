"""
global: variable in a global scope (outside of the function)
local: variable inside a function
nonlocal: in nested function where local function not declared
"""
class apni_class:
    def __str__(self):
        return 'hello'


a = apni_class()
print(a, type(a))


def my_func():
   def fun1():
       global x
       x = 32
   def fun2():
       nonlocal x
       x = 100
   def fun3():
       x = 0
   x = 2
   fun1()
   print(x)
   fun2()
   print(x)
   fun3()
   print(x)

x = 1  # global scope
my_func()
print(x)










