# print pattern of # in 4*5
'''using while
i = 1
while i<=4:
    print('#',end= '')
    j = 1
    while j<5:
        print(' #',end = '')
        j += 1
    i +=1
    print()
-------------------
for i in range(1,5):
    for j in range(1,5):
        if i <= j:
            print(j,end = '')
    print()
----------
apqr
abqr
abcr
abcd



l1 = ['a','b','c','d']
l2 = ['p','q','r']
for i in l1:
    print(i, end='')
    for j in l2:
        print(j,end = '')
    print()

    '''
# add two arrays using loop
import numpy as np

a1 = np.array([1,2,3,5])
a2 = np.array([3,4,5,6])
res = []
c = a1+ a2
print(c)
print(type(c))
for i in range(len(a1)):
    for j in range(len(a2)):
        if i == j:
            res.append(a1[i] + a2[j])
print(res)
print(type(res))







