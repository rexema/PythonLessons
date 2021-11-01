for i in range(101):
    a = list(str(i))
    if i == 1:
        print(i, "процент")
    elif i < 10 and 1 < i < 5:
        print(i, "процента")
    elif 4 < i < 21:
        print(i, "процентов")
    elif i > 20 and int(a[1]) == 0:
        print(i, "процентов")
    elif i > 20 and int(a[1]) == 1:
        print(i, "процент")
    elif i > 20 and 1 < int(a[1]) < 5:
        print(i, "процента")
    elif i > 20 and int(a[1]) > 4:
        print(i, "процентов")
