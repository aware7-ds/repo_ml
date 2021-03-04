# print fib series

def fib(n):
    if n>1:
        val = [0,1]
        a = 1
        for i in range(0,n):
            a += val[i] # 0,1,1,2,
            val.append(a)
        return val
    elif n==1:
        return [0,1]
    else:
        print('enter +ve num')

# 1,1,2,3,5,8,13

num = int(input('enter num:'))
values = fib(num)
print(values)