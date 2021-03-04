# find all prime num in list

val1 = [3,5,9,14,43,24]

ls = []
for ele in val1:
    flag = 0
    for i in range(2,ele+1):
        if ele%i == 0:
            flag += 1
            if flag > 1:
                break
    if flag == 1:
        ls.append(ele)
print('prime:',ls)
