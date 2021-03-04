# lambda func - anonymous
# filter,map,reduce


from functools import reduce

x = [1,2,3,4,5,6]
even = list(filter(lambda x:  x%2 ==0 ,x))
print(even)
sq = list(map(lambda x: x**2,x))
print(sq)
sum = reduce(lambda i,j:i+j,x)
print(sum)

res = list([lambda i: i*i for i in range(7)])
print(res)