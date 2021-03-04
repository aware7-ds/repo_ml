# print all values from 1-100 and skip the numbers divisible by 3 or 5

i = 1
ls = []
while i<=100:
    if i%3 != 0 and i%5 != 0:
        ls.append(i)
    i += 1
print(ls)
print(len(ls))