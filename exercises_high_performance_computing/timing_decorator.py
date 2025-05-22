import time


def timing(func):
    def inner (*args, **kwargs):
        print(f"function {func.__name__} with {args, kwargs}")
        start= time.time()
        result= func(*args,**kwargs)
        end=time.time()
        duration= end - start
        print(f"took {duration}")
        return result 
    return inner
    
@timing
def foo(x,y):
    time.sleep(0.5)
    return x+y

foo(1,2)

