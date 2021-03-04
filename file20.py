# usage of modules

# write all custom functions( prefer returnable func) in a module and reuse it in another

#import file17
#x = file17.fact(7)

#from file17 import *
#x = fact(6)

from file17 import fact
x = fact(5)
print(x)