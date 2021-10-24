from functools import wraps


def type_logger_wrapper(func):
    @wraps(func)
    def type_logger(args):
        result = func(args)
        print(f'{args}: {type(args)}')
        return result

    return type_logger


def func_name_wrapper(func):
    @wraps(func)
    def func_name(args):
        print(f'{func.__name__}')

    return func_name


@type_logger_wrapper
@func_name_wrapper
def calc_cube(x):
    """some function for calc x"""
    return x ** 3


a = calc_cube(2)
