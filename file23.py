# iterators - fetch one value at a time; use iter() and next()
# generators - use yield instead of return in a func
'''
x = [1,2,3,4,5]
res = iter(x)
print(res.__next__())
print(res.__next__())
print(next(res))
'''

def gen(n): # instead of storing all values ,it stores only one value in cache at a time
    for i in range(n):
        yield i
res = gen(6)
print(res)
print(res.__next__())
print(next(res))
