import numpy as np

ar1 = np.array([
                [1,2,3],
                [4,5,6]
            ])
ar2 = np.array([
    [1,2,4],
    [5,6,7]
])

print(ar1.dtype)
print(ar1.ndim)
print(ar1.flatten()) # convert anything to 1D
print(ar1.reshape(3,2)) # converts anything in rows*columns format
print(ar1.ravel())

#a1 = matrix(ar1)
#a2 = matrix(ar2)


#print(a1+a2)
