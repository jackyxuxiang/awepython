import functools

def log(func):
    print('log1')
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def foo():
    print('hello world foo')

@log
def foo1():
    print('hello world foo1')

foo()
foo1()