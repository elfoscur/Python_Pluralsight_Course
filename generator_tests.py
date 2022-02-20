def computation(x):
   return x
 
def consumer():
    while True:
        got = yield 
        print('consumer got value {}'.format(got))
       # do something awesome with got
        

cons = consumer()
next(cons) # prime coroutine

for i in range(10):
   cons.send(computation(i))


print(10%3)
