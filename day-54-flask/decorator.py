import time


def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        end_time = time.time()
        spend_time = end_time - current_time
        print(f"{function.__name__} {spend_time}")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()
