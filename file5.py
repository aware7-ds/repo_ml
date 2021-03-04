# find given num is prime

val1 = int(input('val1:'))
flag = 0

for i in range(2,val1+1):
    if val1%i == 0:
        flag += 1
        if flag > 1:
            break
if flag == 1:
    print('prime')
else:
    print('no prime')
