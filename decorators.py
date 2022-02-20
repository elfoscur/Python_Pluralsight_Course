'''
https://realpython.com/primer-on-python-decorators/
'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee) # return the function wrappper
print(say_whee) # <function my_decorator.<locals>.wrapper at 0x000002BD2822DA60>
say_whee() # execute the function wrapper
# Something is happening before the function is called.
# Whee!
# Something is happening after the function is called.



@my_decorator  # this is equivalent to my_decorator(say_whee)
def say_whee():
    print("Whee!")


say_whee()



def do_twice(func):
    def wrapper_do_twice(*arg, **kwargs):
        func(*arg, **kwargs)
        func(*arg, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")



say_whee() # Whee!\n Whee!


@do_twice
def greet(name, surname):
    print(f"Hello {name} {surname}")


greet("Jhonny","Walker")