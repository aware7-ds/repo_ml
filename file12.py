# variable length arguments
def add(a,*b): ## here b is a tuple and can store multiple arguments in the form of tuple
    print(a)
    print(b)
    c = a
    for i in b:
        c += i
    print(c)

add(2,3,0,9)
#add(2,3)

## keyword variable length arguments - when u dont knw hw many values to be passed

def person(**val):

    for k,v in val.items():
        print(k,v)


person(name = 'moni',age = 28, sal = '<9L')