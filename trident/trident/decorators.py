import functools


def test_decorator(function):
    @functools.wraps(function)
    def wrapper(request,*args,**kwargs):
        print('hello raju')
        return function(request,*args,**kwargs)
    return wrapper