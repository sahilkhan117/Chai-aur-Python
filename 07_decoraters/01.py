# time function calculate

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} run in {end-start} seconds time")
        return result
    return wrapper

@timer
def test():
    time.sleep(2)

test()