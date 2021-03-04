# pass list to a func and count #even n #odd

import numpy as np
def count(l):
    x = y = 0
    for i in l:
        if i%2 == 0:
            x += 1
        else:
            y += 1
    return x,y

lst = np.arange(10)
even,odd = count(lst)
print(even)
print(odd)

# pass list of names to a func and get the names only with letter count >5

def names(lt):
    counts = []
    for i in range(len(lt)):
        if len(lt[i]) > 5:
            counts.append(lt[i])
    return counts

lst= ['moni','hasu','rimpy','charan']
l = names(lst)
print(l)
