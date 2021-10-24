src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def num_gen(src):
    new_list = []
    for num in src:
        num_index = src.index(num)
        if num > int(src[num_index - 1]):
            new_list.append(num)
    print(new_list[1:])


num_gen(src)
