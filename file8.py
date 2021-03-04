# find max value in array

import numpy as np

a = np.array([43,7,67,94,102,87,4,63,453,354,243,987,564])
print(max(a))
i = 0
temp = a[0]
'''
----------------------------
while i<len(a):
    if a[i]>temp:
        temp = a[i]
    i +=1
print(temp)
----------------------------
for i in range(len(a)):
    if a[i]>temp:
        temp = a[i]
print(temp)
---------------------------
'''
b = np.sort(a)
print(a)
print(b)
print(b[-1])

