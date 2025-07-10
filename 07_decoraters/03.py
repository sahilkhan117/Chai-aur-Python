# Cache return function
# store fn result if recall return previous result

import time


def cache(func):
    cache_val = {}

    def wrapper(*args, **kwargs):
        print(cache_val)
        if args in cache_val: # Base case
            return cache_val[args]
        
        result = func(*args, **kwargs)
        cache_val[args] = result
        return result
    return wrapper


@cache
def DBcall(a, b):
    time.sleep(4)
    return a + b


print(DBcall(2, 3))
print(DBcall(2, 3))
print(DBcall(4, 4))
print(DBcall(4, 4))