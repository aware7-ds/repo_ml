# recursion - a function calling itself
'''
def wish():
    global i
    i += 1
    print('Hi Moni',i)
    wish()

i = 0
wish()
'''

# find factorial of num using recursion
# set terminating condition # check file20

def fact(n):
    if n == 0:
        op = 1
    else:
        op = n * fact(n - 1)
    return op

n = 4
res = fact(n)
print(res)
