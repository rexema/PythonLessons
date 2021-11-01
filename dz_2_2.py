list1 = [number ** 3 for number in range(1000) if number % 2 != 0]
new_list = []
for i in list1:
    i = i + 17
    a = list(str(i))
    b = 0
    for j in a:
        j = int(j)
        b = b + j
    if b % 7 == 0:
        new_list.append(i)
d = 0
for i in new_list:
    d = d + i

print(d)
