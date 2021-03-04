# sorting and searching
import numpy as np
ls = [ 23, 54, 65,12, 9, 43, 69]
val1 = int( input('num:'))
ls_new = np.sort(ls)
flag = 0
for ele in ls:
    if val1 == ele:
        flag = 1
        break
if flag == 1:
    print('found')
else:
    print('not found')



