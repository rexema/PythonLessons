from functools import wraps


def vaL_checker(decorator_checker_func):

    def _val_cheker(func_calc_cube):
        @wraps(func_calc_cube)
        def wrapper(x):
            if decorator_checker_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)

        return wrapper

    return _val_cheker


@vaL_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(-5)
print(a)
