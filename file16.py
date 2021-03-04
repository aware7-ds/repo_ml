# factorial

num = int(input('val:'))

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    print(res)

fact(num)