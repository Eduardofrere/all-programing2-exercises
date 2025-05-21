def my_decorator(function):
    def inner(*args, **kwargs):
        print(f"{function.__name__ } was called with argument {args} ")
        return function(*args,**kwargs)
    return inner 

@my_decorator
def foo(a):
    return 2 * a

a = foo(2)
b = foo(4)
c = foo(12)