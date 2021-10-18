list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list2 = []
for i in list1:
    if True == i.isdigit() and int(i) < 10:
        list2.append('"')
        list2.append("0" + i)
        list2.append('"')
    elif i.isdigit() == True and int(i) > 10:
        list2.append('"')
        list2.append(i)
        list2.append('"')
    elif "+" in i:
        for j in i:
            if j != "+":
                list2.append('"')
                list2.append("+" + "0" + j)
                list2.append('"')
    else:
        list2.append(i)
print(" ".join(list2))
