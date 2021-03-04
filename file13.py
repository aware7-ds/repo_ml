# global vs globals

def func():
    # global x
    x = 10
    globals()['x'] = 12
    print('in func:',x)

x= 15
func()
print('out:',x)