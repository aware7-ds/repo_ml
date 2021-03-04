# function that doesnt return any
# function that returns one or more --- needs to be assigned to some var while calling this func
# no pass by val o pass by ref here in python, instead, it depends on what we pass..mutable or immutable obj

import re

s1 = 'hi moni7 ..y r u disturbed?[]/'

def clean(str):
    st = re.sub('[^a-z0-9\s]','',str)
    print(st)
    return(st)

st1 = clean(s1)
print(st1)
print(type(s1))






