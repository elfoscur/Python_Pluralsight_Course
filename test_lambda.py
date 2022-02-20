'''
https://realpython.com/python-lambda/
'''


f = lambda x: x +1 #f is a function (created with a labda expression)
print(type(f))
# it's possible to apply the function to an argument by surrounding the function 
# and it's argument with parentheses
num = f(10) # = (lambda x: x + 1)(2) = lambda 2: 2 + 1
print(num) # 11


ff = lambda a, b: a + b
print(ff(10,20))
print((lambda a, b: a + b)(4, 5))


# high order function
# https://en.wikipedia.org/wiki/Higher-order_function
# In mathematics and computer science, a higher-order function is a function that does at least one of the following:
# takes one or more functions as arguments (i.e. a procedural parameter, which is a parameter of a procedure that is itself a procedure),
# returns a function as its result.


high_order_function = lambda x, func: x + func(x)
res = high_order_function(2, lambda x: x * x)
print(res) # 2 + lambda x: x * x = 2 + 2 * 2 = 6
res = high_order_function(2, lambda x: 2 * 2 * 2)
print(res) # 2 + 2 * 2 * 2 = 10



def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(10) # => lamda x: x + 10
print(type(f)) # class 'function'
print(f(5)) # lamda 5: 5 + 10 = 15


res = (lambda *args : sum(args))(1, 2, 3, 4)
print(res) # 10

res = (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)
print(res) # 6


l = list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
print(l) # ['CAT', 'DOG', 'COW']