# *args and **kwargs:
# *args is used to pass a variable number of non-keyword arguments to a function.
# **kwargs is used to pass a variable number of keyword arguments to a function.

def func(*args,**kwargs):
    print("args:",args)
    print("kwargs:",kwargs)

print(func(1,2,3,4,5,name="John",age=30))