def num_generator(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


nums_gen = num_generator(20)
print(next(nums_gen))
print(next(nums_gen))
print(next(nums_gen))