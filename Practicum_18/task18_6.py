def print_result(func):
    def wrapper(arg):
        result = func(arg)
        print(result)
        return result
    return wrapper

@print_result
def square(x):
    return x * x

square(5)