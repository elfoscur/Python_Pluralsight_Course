def some_decorator(f):
    def wraps(*args):
        print(f"Calling function {f.__name__}")
        return f(args)
    return wraps



@some_decorator
def decorated_function(x):
    print(f"With argument {x}")





test = decorated_function(10,20,30,40) 
# Calling function decorated_function
# With argument (10, 20, 30, 40)